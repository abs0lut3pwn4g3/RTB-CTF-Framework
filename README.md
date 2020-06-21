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

A fast, efficient and lightweight (~100 KB) Capture The Flag framework (in Flask) inspired by the [HackTheBox](https://hackthebox.eu/) platform.

The 100 second elevator-pitch is that: A Capture The Flag framework; one that is fast yet feature packed, efficient thus scalable, lightweight (insert some more pro developer adjectives) and customizable to your organization's brand while not emptying your bank A/C.


**Want to see it in action?**

   A live demo of the app is available at: <https://rtblivedemo.herokuapp.com/>.

   You can login and mess around as the admin user `admin:admin` (i.e. username:password combinations) or register your own.

## Features

* Machines listing with fields: name, IP, OS, points and difficulty level.
* Challenges listing with fields: title, description, URL, points.
* Totally configurable settings such as running time, organization details, CTF name, etc.
* Automatic strong password for administrator
* Well implemented controls for administrators providing features such as issuing notifications, database CRUD operations, full fledged logging,
* Simple User Registration/login process, account management, Forgot password functionalities,
* Flag submission (currently 2 flags: user and root),
* Real time scoreboard tracking,
* Efficient caching so it's fast
* Easily deployable on Heroku.

## Build locally

Please see [INSTALLATION.md](INSTALLATION.md).

## Host a customized CTF with Heroku for free in under a minute

1. Sign up on [Heroku](https://heroku.com), if you haven't already and click on the below "Deploy to Heroku" button.

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

2. Give your application an awesome name and _optionally_ specify mail environment variables.
    
    > Note: A psuedo-random password for the **admin** user would be created and set in the config variable `ADMIN_PASS`. On Heroku, you can reveal this password from your application's dashboard settings. Same for the Flask application's `SECRET_KEY`.

3. Open your newly deployed application in the browser, you'll be redirected to login as the `admin` user and do so.

4. Finally, you'll want to `/setup` the CTF Settings and,

#### Yay! Now you have a customized instance of the RTB-CTF-Framework live on Heroku. 🎉

> Bonus: You can manage the database CRUD operations from admin views GUI; change machine settings, issue notifications to users, etc.

## Inspiration

The main purpose of this project is to serve as a scoring engine and CTF manager. One that is packed with features, can handle enterprise/global level traffic on a scalable yet free heroku's dyno.

[CTFd](https://github.com/ctfd/ctfd) is one of the most popular CTF framework and we have used it for multiple engagements and will surely use it again. But at the same time, CTFd is heavy (~22.2 mb) (it gives poor performance even on a $49/mo heroku dyno) and not everyone has $$$ to spend on cloud, especially students (like us). So, that's where RTB-CTF-Framework (~100 KB) comes in.

## Contributing

<p>
  <a href="https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/graphs/contributors">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/abs0lut3pwn4g3/RTB-CTF-Framework?color=red&logo=github&style=for-the-badge">
  </a>
</p>


##### Join us on slack

- [#rtb-ctf-framework on slack](https://rtb-ctf-framework.slack.com)

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md)


## Live Demo

**Live Demo:** <https://rtblivedemo.herokuapp.com/> (login with `admin:admin`)
