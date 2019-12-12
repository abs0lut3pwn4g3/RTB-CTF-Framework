# RootTheBox CTF Framework

[![Rawsec's CyberSecurity Inventory](https://inventory.rawsec.ml/img/badges/Rawsec-inventoried-FF5050_for-the-badge.svg)](https://inventory.rawsec.ml/)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

A CTF framework(in flask) for HackTheBox style machines. <br/>
The main purpose of this project is to serve as a scoring engine and CTF manager.
A live demo of the app is available at: https://rtblivedemo.herokuapp.com/. <br/>
You can login and mess around as 2 users: `admin:admin` and `test:test`.(i.e. username:password)

## Features

* Flask Blueprints
* Flask-admin for Admin views and easy realtime management
* Easily deployable on Heroku.
* A page to show relevant details about the machine such as name, IP, OS, points and difficulty level. 
* User Registration, account management, Forgot password, Notifications, Full Fledged Logging
* Hash submission (currently 2 hashes: user and root)
* Real time scoreboard tracking

## How To Use

### Requirements

* `Python 3.7.3` or atleast `> 3.6`.
* Packages: [`src/requirements.txt`](src/requirements.txt).

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

### Deployment using Heroku

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

## For Your CTF

Using this as simple as anything. 

1. Just configure your CTF settings in [`config.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/FlaskRTBCTF/config.py).

2. DO NOT FORGET to change admin credentials from [`create_db.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/create_db.py)

3. See database instance creation steps under How To Use.

Bonus: You can manage the database CRUD operations from admin views GUI as well as issue notifications. 

> Warning: If you make any change to [`config.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/FlaskRTBCTF/config.py) logging/config class/score settings. It's highly recommended to create a new DB instance.

## Contributing

Please see: [issues](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues) and the below To-do list

## To-do

- [ ] Freeze Scoreboard automatically past running time specified
- [ ] Support for more hashes
- [ ] Testing Password reset functionality
- [ ] More info for `home.html`
- [ ] Need to implement `account.html` (not a priority)

<hr/>

- [x] db relationship between User and Score Tables (priority | issue: #5)
- [x] isAdmin column in User table and Admin views (priority)
- [x] Notifications
- [x] Use Flask Blueprints
- [x] Finalize black theme?
- [x] Error messages not appearing in `/submit`
- [x] Implement `machine.html` to server a page where one can download/serve machines


## Screenshots

<img src="screenshots/home_ss.png" width=400 />
<img src="screenshots/scoreboard_ss.png" width=400 />
<img src="screenshots/machine_ss.png" width=400 />

