# Installation / How To Use

### Requirements

* Tested on `Python 3.8.2`
* Python Packages: [`src/requirements.txt`](src/requirements.txt).
* OS Packages: PostgreSQL version 11 or greater, `libpq-dev`, `python3-dev` packages. Please refer [here](https://tutorials.technology/solved_errors/9-Error-pg_config-executable-not-found.html).

### Build locally and run

1. Git clone the repo and `cd ` into it

```bash
$ git clone https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework
$ cd RTB-CTF-Framework/
```
2. Create `virtual environment` to deal with dependencies and requirements.

```bash
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
$ cd src/
```

3. With `virtual environment` activated, install requirements, init db and run !

```bash
[venv]$ pip install -r requirements.txt 
[venv]$ python create_db.py # Only required on first run
[venv]$ python run.py
```

> Warning: If you make any change to [`config.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/FlaskRTBCTF/config.py) logging/config class/score settings. It's highly recommended to create a new DB instance.

### Docker

> Note: The Docker support is not tested for production yet. It's recommended to use Heroku for production.

```bash
$ docker-compose up
```
