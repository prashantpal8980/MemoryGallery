# 🚀 Memory Gallery – Django Deployment Guide

A high-performance Django application for managing personal galleries, optimized for **Oracle Cloud Always Free Tier** using a production-ready stack: **Gunicorn + Nginx + SSL**.

---

## 📌 Tech Stack

* **Framework:** Django (Python 3.10+)
* **WSGI Server:** Gunicorn
* **Reverse Proxy:** Nginx
* **SSL Certificate:** Let's Encrypt (Certbot)
* **Infrastructure:** Oracle Cloud VPS (Ubuntu 24.04 LTS)
* **Database:** SQLite (Default)
* **Live URL:** [https://prashantpal.online](https://prashantpal.online)

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
ALLOWED_HOSTS = ['domain']
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
    server_name prashantpal.online www.prashantpal.online;

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
sudo service iptables save
sudo netfilter-persistent save
```

### Oracle Cloud Ingress Rules

| Protocol | Port | Source      |
| -------- | ---- | ----------- |
| TCP      | 80   | 0.0.0.0/0   |
| TCP      | 443  | 0.0.0.0/0   |

---

## 🔒 Step 7: HTTPS / SSL Setup (Let's Encrypt + Certbot)

This site is secured using **Let's Encrypt** and **Certbot** for Nginx.

### 1. Install Certbot and the Nginx plugin

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y
```

### 2. Obtain and install the SSL certificate

```bash
sudo certbot --nginx -d prashantpal.online -d www.prashantpal.online
```

Certbot will automatically:
- Verify domain ownership via HTTP challenge
- Obtain a free SSL certificate from Let's Encrypt
- Modify your Nginx config to redirect HTTP → HTTPS

### 3. Verify auto-renewal

Let's Encrypt certificates expire every 90 days. Certbot installs a systemd timer to handle renewal automatically. Test it with:

```bash
sudo certbot renew --dry-run
```

### 4. After SSL setup — update Django settings

```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## 🌍 Final Result
https://prashantpal.online

---

## ⚠️ Common Issues

| Issue                  | Solution                              |
| ---------------------- | ------------------------------------- |
| 502 Bad Gateway        | Check Gunicorn socket path            |
| Permission denied      | Fix directory permissions             |
| Static not loading     | Run `collectstatic`                   |
| Site not reachable     | Open ports 80 and 443                 |
| SSL certificate error  | Re-run `certbot --nginx`              |
| Certbot renewal fails  | Ensure port 80 is open for challenges |

---

## 🚀 Future Improvements

* [x] Add HTTPS (Certbot SSL) ✅
* [x] Connect custom domain ✅
* [ ] Use PostgreSQL
* [ ] Add CI/CD pipeline
* [ ] Set up automated backups

---

## 👨‍💻 Author

**Prashant Pal**
Cybersecurity Enthusiast | Django Developer
🌐 [prashantpal.online](https://prashantpal.online)
