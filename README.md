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
  <a href="https://lgtm.com/projects/g/abs0lut3pwn4g3/RTB-CTF-Framework/context:python">
  	<img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/abs0lut3pwn4g3/RTB-CTF-Framework.svg?logo=lgtm&logoWidth=18"/>
  </a>
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

* Machines listing name, IP, OS, points and difficulty level.
* Challenges listing with title, description, URL, points.
* Totally configurable settings such running time, organization details, CTF name.
* Automatic strong password for administrator
* Well implemented controls for administrators providing features such as issuing notifications, database CRUD operations, full fledged logging,
* Simple User Registration/login process, account management, Forgot password functionalities,
* Flag submission (currently 2 flags: user and root),
* Real time scoreboard tracking,
* Efficient caching so it's fast
* Easily deployable on Heroku. 

## Build locally

Please see [INSTALLATION.md](INSTALLATION.md).

## Host Your Own CTF in a minute with Heroku

1. Sign up on [Heroku](https://heroku.com), if you haven't already and click on the below "Deploy to Heroku" button.

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

2. Give your application an awesome name and _optionally_ specify mail environment variables.
    
    > Note: A psuedo-random password for the **admin** user would be created and set in the config variable `ADMIN_PASS`. On Heroku, you can reveal this password from your application's dashboard settings. Same for the Flask application's `SECRET_KEY`.

3. Open your newly deployed application in the browser, you'll be redirected to login as the `admin` user and do so.

4. Finally, you'll want to `/setup` the CTF Settings and,

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

## Live Demo

** Live Demo: <https://rtblivedemo.herokuapp.com/> (login with `admin:admin`)
