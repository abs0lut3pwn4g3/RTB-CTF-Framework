# RootTheBox CTF Framework

A CTF framework(in flask) for HackTheBox style machines. 

## Features

* Flask Blueprints
* Easily deployable on Heroku.
* User Registration, account management, Forgot password
* Hash submission (currently 2 hashes: user and root)
* Real time scoreboard tracking
* A page to show relevant details about the machine such as name, IP, OS, points and difficulty level. 

## How To Use

### Requirements

* `Python 3.7.3` or atleast `> 3.6`.
* Packages: [`src/requirements.txt`](src/requirements.txt).

```bash
$ git clone https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework
$ cd RTB-CTF-Framework/src/
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
[venv]$ pip install -r requirements.txt 
[venv]$ python run.py
```

Using this as simple as anything. Just configure your CTF settings in [`config.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/FlaskRTBCTF/config.py).

#### Creating database instance file

Locally or for docker,

```bash
$ source venv/bin/activate
$ python3 # open python interpreter
>>> from FlaskRTBCTF import db, create_app
>>> db.create_all(app=create_app())
```

For Heroku, 

```bash
$ heroku run python
>>> from FlaskRTBCTF import db, create_app
>>> db.create_all(app=create_app())
```

## To-do

- [ ] isAdmin column in User table and Admin views (priority)
- [ ] Support for more hashes
- [ ] Testing Password reset functionality
- [ ] Notifications
- [ ] More info for `home.html`
- [ ] Need to implement `account.html` (not a priority)

<hr/>

- [x] Use Flask Blueprinsts
- [x] Finalize black theme?
- [x] Error messages not appearing in `/submit`
- [x] Implement `machine.html` to server a page where one can download/serve machines
- [x] Add basic info and stuff to `layout.html`
- [x] User is able to submit hash multiple times and keep increasing score, so need to implement limitations


## Screenshots

<img src="screenshots/home_ss.png" width=400 />
<img src="screenshots/scoreboard_ss.png" width=400 />
<img src="screenshots/machine_ss.png" width=400 />
