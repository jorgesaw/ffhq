# ffhq
Firefighter Headquarter



### Getting started:

Instalar python si no lo tenes instalado https://www.python.org/downloads/

Descargar el instalador de pip https://bootstrap.pypa.io/get-pip.py

```
user@host:/# python get-pip.py install
```

Instalar virtualenv y activarlo:

```
user@host:# pip install virtualenv
user@host:# virtualenv ffhq --no-site-packages
(ffhq)user@host:# . ffhq/bin/activate
```

Clonar el repo, instalar dependencias:
```
(ffhq)user@host:# git clone git@github.com:edvm/ffhq.git
(ffhq)user@host:# cd ffhq
(ffhq)user@host:# pip install -r requirements.txt
```


Por el momento es necesario instalar crispy-forms-materialize desde el repositor (con el entorno activado):
```
(ffhq)user@host:# git clone git@github.com:edvm/crispy-forms-materialize.gitt
(ffhq)user@host:# python setup.py develop
```

Correr el server:
```
(ffhq)user@host:# python manage.py runserver
```
