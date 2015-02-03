# ffhq
Firefighter Headquarter



### Getting started:

Instalar python si no lo tenes instalado https://www.python.org/downloads/

Descargar el instalador de pip https://bootstrap.pypa.io/get-pip.py

```
python get-pip.py install
```

Instalar virtualenv y activarlo:

```
pip install virtualenv
virtualenv ffhq --no-site-packages
. ffhq/bin/activate
```

Clonar el repo, instalar dependencias:
```
git clone git@github.com:edvm/ffhq.git
cd ffhq
pip install -r requirements.txt
```

Correr el server:
```
python manage.py runserver
```
