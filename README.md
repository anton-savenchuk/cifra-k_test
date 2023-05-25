# Instructions

### Clone repository
```bash
git clone https://github.com/anton-savenchuk/cifra-k_test.git
cd cifra-k_test
```
 
### Build and run docker-compose
```bash
docker-compose up --build
```

### Create an administrator account
```bash
docker exec -it django /bin/bash
poetry run python manage.py createsuperuser
```

### Run
```
http://127.0.0.1:8000
http://127.0.0.1:8000/admin - admin panel
```
