# Tongji

Latest running version [here](https://tongji.herokuapp.com/)
ID Number: admin
Password: admin

## Setup

Setup environment for the first time:
```bash
$ mkdir [my_project_folder]
$ cd [my_project_folder]
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ git init
$ git clone https://github.com/fanghuang/Tongji.git
$ cd Tongji
$ pip install -r requirements.txt
$ python manage.py runserver
open http://127.0.0.1:8000/
$ deactivate
```

Next time when you start coding:
```bash
$ source venv/bin/activate
$ python manage.py runserver
```


When you finish coding:
```bash
$ deactivate
```

Or you can do this instead:
```bash
$ pip install -r requirements.txt
$ python manage.py runserver
