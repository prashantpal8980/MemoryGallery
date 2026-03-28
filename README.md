# 🚀 Memory Gallery – Django Deployment Guide

A high-performance Django application for managing personal galleries, optimized for **Oracle Cloud Always Free Tier** using a production-ready stack: **Gunicorn + Nginx**.

---

## 📌 Tech Stack
* **Framework:** Django (Python 3.10+)
* **WSGI Server:** Gunicorn
* **Reverse Proxy:** Nginx
* **Infrastructure:** Oracle Cloud VPS (Ubuntu 24.04 LTS)
* **Database:** SQLite (Default)

---

## ☁️ Oracle Cloud Free Tier Implementation

This project is designed to run within the **Oracle Always Free** limits. Depending on regional availability, you can use either of these shapes:

### 1. AMD Micro Shape (Current Setup)
* **Shape:** `VM.Standard.E2.1.Micro`
* **Specs:** 1 OCPU, 1 GB RAM
* **Best for:** Lightweight testing and small personal projects.

### 2. ARM Ampere Shape (High Performance)
* **Shape:** `VM.Standard.A1.Flex`
* **Specs:** Up to 4 OCPU, 24 GB RAM
* **Storage:** Up to 200 GB (Balanced Performance VPU 10)
* **Note:** In busy regions like **Mumbai (AP-MUMBAI-1)**, you may encounter "Out of Capacity" errors. Re-try frequently to secure a slot.

---

## 🛠️ Step 1: Server Preparation
Update your system and install essential dependencies:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv nginx git
📂 Step 2: Project Setup
Clone the repository and set up the virtual environment:

Bash
git clone [https://github.com/yourusername/memory-gallery.git](https://github.com/yourusername/memory-gallery.git)
cd memory-gallery
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn pillow
⚙️ Step 3: Django Configuration
Edit settings.py for production:

Python
DEBUG = False
ALLOWED_HOSTS = ['your_server_public_ip']
Run migrations and collect static files:

Bash
python manage.py migrate
python manage.py collectstatic
⚡ Step 4: Gunicorn Systemd Setup
Create a service file to ensure Gunicorn starts automatically:
sudo nano /etc/systemd/system/gunicorn.service

Paste the following configuration:

Ini, TOML
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/memory-gallery
ExecStart=/home/ubuntu/memory-gallery/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/home/ubuntu/memory-gallery/gunicorn.sock \
    memoryGallery.wsgi:application

[Install]
WantedBy=multi-user.target
🌐 Step 5: Nginx Configuration
Create the Nginx reverse proxy config:
sudo nano /etc/nginx/sites-available/memory-gallery

Paste the following:

Nginx
server {
    listen 80;
    server_name your_server_public_ip;

    location /static/ {
        alias /home/ubuntu/memory-gallery/staticfiles/;
    }

    location /media/ {
        alias /home/ubuntu/memory-gallery/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/memory-gallery/gunicorn.sock;
    }
}
Enable the site and restart services:

Bash
sudo ln -s /etc/nginx/sites-available/memory-gallery /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl restart gunicorn
🔐 Step 6: Permissions & Firewall (Important)
Ensure Nginx has permission to access the socket and project files:

Bash
sudo chown -R ubuntu:www-data /home/ubuntu/memory-gallery
sudo chmod 755 /home/ubuntu
Oracle Cloud Ingress Rules
Ensure Port 80 (HTTP) is open in your VCN Security List. On the server, run:

Bash
sudo iptables -I INPUT 6 -p tcp --dport 80 -j ACCEPT
sudo netfilter-persistent save
🌍 Final Result
Your application is now live at: http://your_public_ip

👨‍💻 Author
Prashant Pal
Cybersecurity Enthusiast | Django Developer
