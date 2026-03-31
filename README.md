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

This project is designed to run within the **Oracle Always Free** limits.

### 🔹 1. AMD Micro Shape (Current Setup)

* **Shape:** `VM.Standard.E2.1.Micro`
* **Specs:** 1 OCPU, 1 GB RAM
* **Best for:** Lightweight testing and small personal projects.

---

## 🛠️ Step 1: Server Preparation

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv nginx git
```

---

## 📂 Step 2: Project Setup

```bash
git clone https://github.com/yourusername/memory-gallery.git
cd memory-gallery

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install gunicorn pillow
```

---

## ⚙️ Step 3: Django Configuration

Edit `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['your_server_public_ip']
```

Run:

```bash
python manage.py migrate
python manage.py collectstatic
```

---

## ⚡ Step 4: Gunicorn Setup

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

```ini
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
```

```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

---

## 🌐 Step 5: Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/memory-gallery
```

```nginx
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
```

```bash
sudo ln -s /etc/nginx/sites-available/memory-gallery /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/default

sudo nginx -t
sudo systemctl restart nginx
sudo systemctl restart gunicorn
```

---

## 🔐 Step 6: Permissions & Firewall

```bash
sudo chown -R ubuntu:www-data /home/ubuntu/memory-gallery
sudo chmod 755 /home/ubuntu
sudo iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
```

### Oracle Cloud Ingress Rule

* Source: `0.0.0.0/0`
* Protocol: TCP
* Port: `80`

---

## 🌍 Final Result

```
http://your_public_ip
```

---

## ⚠️ Common Issues

| Issue              | Solution                   |
| ------------------ | -------------------------- |
| 502 Bad Gateway    | Check Gunicorn socket path |
| Permission denied  | Fix directory permissions  |
| Static not loading | Run `collectstatic`        |
| Site not reachable | Open port 80               |

---

## 🚀 Future Improvements

* Add HTTPS (Certbot SSL)
* Connect custom domain
* Use PostgreSQL
* Add CI/CD pipeline

---

## 👨‍💻 Author

**Prashant Pal**
Cybersecurity Enthusiast | Django Developer
