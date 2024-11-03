## WorkersBoard
**simple django website with database, templates, admin-panel and migration**

<h4 align="center">build setup</h4>
<p align="center">(ubuntu-latest)</p>

```
# clone the repo into your disk

$ git clone https://github.com/hellcard/workers_board.git

# installing dependencies

$ cd workers_board
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install django~=4.1
(.venv)$ cd web

# server startup

(.venv)$ python manage.py runserver
```

Now you can view this site. To exit the virtual environment, type
```
(.venv)$ deactivate
$ 
```

<h4 align="center">The following routes are available:</h4>

1. "admin/" - admin panel

2. "" - home page

3. "board/" - board with workers


<h2 align="center">admin panel</h2>

<h3 align="center">Login: admin</h3>

<h3 align="center">Password: 123</h3>
