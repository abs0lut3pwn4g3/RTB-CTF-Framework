# RootTheBox CTF Framework

<p >
  <a href="https://inventory.rawsec.ml/" target="_blank">
    <img height="26px" alt="Rawsec's CyberSecurity Inventory" src="https://inventory.rawsec.ml/img/badges/Rawsec-inventoried-FF5050_for-the-badge.svg">
  </a>
  <img height="26px" src="https://forthebadge.com/images/badges/made-with-python.svg">
</p>
<p style="height:18px">
  <a href="https://travis-ci.com/abs0lut3pwn4g3/RTB-CTF-Framework" target="_blank">
    <img alt="Build Status" src="https://travis-ci.com/abs0lut3pwn4g3/RTB-CTF-Framework.svg?branch=gssoc20-dev"/>
  </a>
  <!-- <a href="https://lgtm.com/projects/g/abs0lut3pwn4g3/RTB-CTF-Framework/context:python">
  	<img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/abs0lut3pwn4g3/RTB-CTF-Framework.svg?logo=lgtm&logoWidth=18"/>
  </a> -->
  <a href="https://github.com/psf/black" target="_blank">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/>
  </a>
</p>

A lightweight, easy to deploy CTF framework (in Flask) for HackTheBox style machines.

The main purpose of this project is to serve as a scoring engine and CTF manager.

**Want to see it in action?**

   A live demo of the app is available at: <https://rtblivedemo.herokuapp.com/>.

   You can login and mess around as 2 users: `admin:admin` and `test:test` (i.e. username:password combinations)

## Features

##### For CTF hosters
* A page to show relevant details about the machine such as name, IP, OS, points and difficulty level. 
* Automatic strong password for administrator
* Well implemented controls for administrators providing features such as issuing notifications, database CRUD operations, full fledged logging,
* Simple User Registration/login process, account management, Forgot password functionalities,
* Flag submission (currently 2 flags: user and root),
* Real time scoreboard tracking,
* Easily deployable on Heroku. 

##### For Developers & Contributors
* Flask-blueprints for modularity and clean codebase,
* Flask-admin for Admin views and easy realtime management,
* Flask-SQLAlchemy for SQL models, 
* Flask-wtf for forms,
* Flask-mail for mail service.

## Deployment 

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

or do it manually,

1. Create your heroku app using `heroku` cli tool.
   
   Follow the official guide by Heroku: https://devcenter.heroku.com/articles/getting-started-with-python#prepare-the-app

2. Provision Database add-on.
   
   Add the following add on to your new app: https://elements.heroku.com/addons/heroku-postgresql
   
3. Creating database instance. In your heroku app directory,

   ```bash
   $ heroku run bash
   [heroku]$ python create_db.py
   ```
4. Your app should be live now. You can run `heroku open` to open it in browser.

### Docker

```bash
$ docker-compose up
```

## How To Use

### Requirements

* Tested on `Python 3.8.2`
* Python Packages: [`src/requirements.txt`](src/requirements.txt).
* OS Packages: PostgreSQL version 11 or greater, `libpq-dev`, `python3-dev` packages. Please refer [here](https://tutorials.technology/solved_errors/9-Error-pg_config-executable-not-found.html).

### Installation and first run

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

### Configuration For Your CTF

Using this as simple as anything.

1. Just configure your CTF settings in [`config.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/FlaskRTBCTF/config.py).

2. When you run [`create_db.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/create_db.py), a strong and random 16 char password for the **admin** user is created and set in the environment variable `ADMIN_PASS`. On Heroku, you can reveal this password from your application's dashboard settings.

3. See database instance creation steps under How To Use.

Bonus: You can manage the database CRUD operations from admin views GUI as well as issue notifications. 

> Warning: If you make any change to [`config.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/FlaskRTBCTF/config.py) logging/config class/score settings. It's highly recommended to create a new DB instance.

## Contributing

<p>
  <a href="https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/graphs/contributors">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/abs0lut3pwn4g3/RTB-CTF-Framework?color=red&logo=github&style=for-the-badge">
  </a>
  <a href="https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues?q=is%3Aopen+is%3Aissue+label%3Agssoc20">
  	<img alt="GitHub issues by-label" src="https://img.shields.io/github/issues/abs0lut3pwn4g3/RTB-CTF-Framework/gssoc20?color=deeppink&style=for-the-badge">
  </a>
</p>


##### 👨 Project Owner

- Eshaan Bansal ([github](https://github.com/eshaan7), [linkedin](https://www.linkedin.com/in/eshaan7/))

##### 👬  Mentors

- Sombuddha Chakravarty ([github](https://github.com/sammy1997), [linkedin](https://www.linkedin.com/in/sombuddha-chakravarty-9482b5131/))

##### Slack Channel for GSSoC 2020

- [#proj_root-the-box-ctf-framework](https://app.slack.com/client/TRN1H1V43/CUC71PDD2)

For further guidelines, Please refer to [CONTRIBUTING.md](CONTRIBUTING.md)

## Screenshots

<img src="screenshots/home_ss.png" width=400 />
<img src="screenshots/scoreboard_ss.png" width=400 />
<img src="screenshots/machine_ss.png" width=400 />

