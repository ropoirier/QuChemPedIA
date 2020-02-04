
# Mise en place de l'environement

## Installation avec vagrant

### Mise en place de la VM vagrant
```
vagrant up
```
Cette commande va échouer car les *VirtualBox Guest Additions* ne sont pas installées et il est donc impossible de monter les shared folders et de terminer le provisionning
```
vagrant provision
```
Cette commande va installer toutes les dépendances nécessaires
```
vagrant reload --provision
```
Enfin, cette commande va relancer la VM pour installer les *VirtualBox Guest Additions* et va terminer le provisionning (installation des requirements, yarn) qui n'était pas possible

### Configuration de la base de données
Comme il n'est pas possible d'intégrer facilement cette partie au Vagrantfile, il faut exécuter les commandes suivantes à la main :
```
vagrant ssh
sudo su
su - postgres
psql -c 'create database "QuChemPedIADB"'
psql -c 'CREATE ROLE "dataSlave"'
psql -c "ALTER ROLE \"dataSlave\" WITH NOSUPERUSER INHERIT CREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'P@ssw0rd' VALID UNTIL 'infinity'"
psql -c "GRANT ALL ON DATABASE \"QuChemPedIADB\" TO \"dataSlave\""
exit
exit
```

### Lancement du projet
Il est maintenant possible d'accéder au code source du projet à partir du dossier /src/ de la VM
```
vagrant ssh
cd /src/
```
Pour lancer l'application, il faut lancer la commande suivante :
```
cd /src/QuChemPedIAProject/
python3 manage.py runserver 0:8000
```
Le site est alors accessible à l'adresse **192.168.33.10:8000** directement depuis votre poste

## Installation avec VirtualEnv (ancienne méthode)

### pour commencer mettons à jour notre système :
	 sudo apt-get update && apt-get upgrade -y

### installation de postgreSQL ([CF](https://www.howtoforge.com/tutorial/ubuntu-postgresql-installation/))
	sudo apt-get -y install postgresql postgresql-contrib phppgadmin

### installation de virtualenv with python3
	cd /location
	virtualenv -p python3 nameOfEnv
	source /path/to/the/directory/of/env

### installation de django
	pip install django

### to Generate a requirements file
	pip freeze > requirements.txt

### to Install the packages
	pip install -r requirements.txt

### to relocate the virtual env
	virtualenv --relocatable ENV

### installation du module de communication avec postgre
	pip install psycopg2-binary

### Read the doc here :
	https://virtualenv.pypa.io/en/stable/userguide/

### installation des d'open babel
	apt-get install openbabel libopenbabel-dev swig

### installation des librairie python

	./install_venv.sh

## Configuration
### creation du superutilisateur django
	python manage.py createsuperuser

### Set up database :
	create an user : "dataSlave", password : "P@ssw0rd"
	and a database : "QuChemPedIADB"
	to ask django to set up the connection with database :
	python manage.py makemigrations QuChemPedIA
	python manage.py migrate
	
## Front End assets

### Package manager : yarn

Pour installer yarn, voir https://yarnpkg.com/en/docs/install

Yarn requiert [NodeJs](https://nodejs.org/en/)

### Installation des dépendences

```
yarn
```

### Compilation des assets js et css

Pour le dévelopement :
```
yarn dev
```

Pour la production :
```
yarn build
```

## Release

To release the develop branch onto master:

```bash
git checkout develop
```

Start your release branch
```bash
git flow release start [version-tag]
```

Build front end assets for production
```bash
yarn build
```

Commit the compiled assets
```bash
git add QuChemPedIAProject/common_qcpia/static/dist/*
git commit -m "release: Compiled front end assets"
```

Finish the release

```bash
git flow release finish
```

