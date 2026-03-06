server {
    server_name kalton.carlkasa.com;

    # Increase client max body size for file uploads
    client_max_body_size 100M;


    # Static files - collected at STATIC_ROOT
    location /static/ {
        alias /home/tarimo/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Media files
    location /media/ {
        alias /home/tarimo/media/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Main application - proxy to Gunicorn on port 8000
    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
        
        # Important: Pass these headers to Django
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Increase timeout for large requests
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/kalton.carlkasa.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/kalton.carlkasa.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

# HTTP redirect
server {
    if ($host = kalton.carlkasa.com) {
        return 301 https://$host$request_uri;
    }

    listen 80;
    server_name kalton.carlkasa.com 31.220.75.145;
    return 301 https://$server_name$request_uri;  # Changed from 404 to redirect
}