# django-rest-vue-template

Simple SPA template of django and vue.
ServerSide: django
FrontSide:  Vue.js

## Installation

1. Go https://github.com/Saknowman/django-rest-vue-template
2. then Download ZIP
3. Remove .git directory.
4. Replace 'project_name' with [Your Project Name] by grep.

## Usage

#### Init Virtual Environment

```bash
$ python -m venv venv
## Windows
$ source ./venv/Scripts/activate
## Mac
$ source ./venv/bin/activate
```

#### Install Libraries

```bash
(venv)$ pip install -r requirements.txt
(venv)$ npm install
```

#### Build Application

```bash
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ npm run build
```

#### Run

```bash
## Run these, if you want develop Server Side.
(venv)$ python manage.py runserver

## Open two terminals and run these, if you want develop Front Side.
## And access localhost:8080.
(venv)$ python manage.py runserver
(venv)$ npm run dev
```

## License

Read ./LICENSE
