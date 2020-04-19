# RootTheBox CTF Framework

<p>
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

   You can login and mess around as the admin user `admin:admin` (i.e. username:password combinations) or register your own.

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
* Flask-login for session handling,
* Flask-wtf for responsive forms,
* Flask-mail for mail service,
* Flask-bcrypt for password hashing and security,

## Build locally

Please see [INSTALLATION.md](INSTALLATION.md).

## Host Your Own CTF In 5 minutes with Heroku

Using this is as simple as anything.

1. Fork the `master` branch and clone your fork,

```bash
$ git clone https://github.com/<your_github_username>/RTB-CTF-Framework
$ cd RTB-CTF-Framework/
```

2. Configure your CTF settings (such as name, running time) in [`config.py`](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/blob/master/src/FlaskRTBCTF/config.py).

3. In the `app.json`, change the `repository` key's value to match your fork's URL.

4. Push these changes to the remote of your fork.

5. Visit your Fork's GitHub URL in the browser and click on the following **Deploy to Heroku** button.
    
    > Note: A psuedo-random password for the **admin** user would be created and set in the config variable `ADMIN_PASS`. On Heroku, you can reveal this password from your application's dashboard settings. Same for the Flask application's `SECRET_KEY`.

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Yay! Now you have a customized instance of the RTB-CTF-Framework live on Heroku. 🎉

> Bonus: You can manage the database CRUD operations from admin views GUI; change machine settings, issue notifications to users, etc.

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

> Why look at static pictures, when you can use a demo ? Visit: <https://rtblivedemo.herokuapp.com/>.

<img src="screenshots/home_ss.png" width=400 />
<img src="screenshots/scoreboard_ss.png" width=400 />
<img src="screenshots/machine_ss.png" width=400 />

