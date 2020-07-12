
# Contributing to RTB-CTF-Framework

<p align="center">
  <a href="https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/graphs/contributors">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/abs0lut3pwn4g3/RTB-CTF-Framework?color=red&logo=github&style=for-the-badge">
  </a>
</p>

<p align="center">
  <a href="https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues?q=is%3Aopen+is%3Aissue+label%3Aeasy">
    <img alt="GitHub issues by-label" src="https://img.shields.io/github/issues/abs0lut3pwn4g3/RTB-CTF-Framework/easy?color=seagreen&style=for-the-badge">
  </a>
  <a href="https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues?q=is%3Aopen+is%3Aissue+label%3Amedium">
    <img alt="GitHub issues by-label" src="https://img.shields.io/github/issues/abs0lut3pwn4g3/RTB-CTF-Framework/medium?color=%23e99695&style=for-the-badge">
  </a>
  <a href="https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues?q=is%3Aopen+is%3Aissue+label%3Ahard">
    <img alt="GitHub issues by-label" src="https://img.shields.io/github/issues/abs0lut3pwn4g3/RTB-CTF-Framework/hard?color=%23cc317c%09&style=for-the-badge">
  </a>
</p>

## This project makes use of the following Flask libraries

* Blueprints for modularity and clean codebase,
* Flask-admin for Admin views and easy realtime management,
* Flask-SQLAlchemy for SQL models,
* Flask-Caching with redis for efficient caching,
* Flask-login for session handling,
* Flask-wtf for responsive forms,
* Flask-mail for mail service,
* Flask-bcrypt for password hashing and security,

## Style Guide

Keeping to a consistent code style throughout the project makes it easier to contribute and collaborate. Please stick to the guidelines in [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) and the Google Style Guide unless there’s a very good reason not to.

### Before submitting a Pull Request, please run these 2 commands locally

```bash
$ black .
```

```bash
$ flake8 src/ --max-line-length=88 --show-source --statistics
```

if flake8 shows any errors or warnings, please fix the changes in a new commit and squash all the commits into one before submitting the PR.

> Guide on squashing commits: [here](https://github.com/wprig/wprig/wiki/How-to-squash-commits)

## Contact

##### Join us on slack

- [#rtb-ctf-framework on slack](https://rtb-ctf-framework.slack.com)

## Where to start ? 

See: [Issues](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues) and the following To-do list. Or just ping one of the mentors with new ideas.

> Note: All PRs should be made against the latest changes in the `develop` branch.

## To-do

- [ ] Ideas for additional logging techniques to prevent flag sharing, cheating and such. (Issue: [#7](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues/7))
- [ ] Dark theme for `admin control` panel. (Issue: [#16](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues/16))
- [ ] Testing Password reset functionality, the mail-server setup, etc.
- [ ] More info on `home.html`
- [ ] Need to implement `account.html`
- [ ] Support for more hashes per box (not a priority)

<hr/>

- [x] Support for *n* number of boxes (accordions? seperate route?). (Issue: [#17](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues/17))
- [x] Rating system: Average Box rating - input, calculate, output. (Issue: [#14](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues/14))
- [x] Freeze Scoreboard automatically past running time specified (Issue: [#3](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues/3))
- [x] Adding a `Deploy to Heroku` button. (Issue: [#15](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues/15))
- [x] Adding CI, Linting, Formatting specs. (Issue: [#18](https://github.com/abs0lut3pwn4g3/RTB-CTF-Framework/issues/18))
- [x] db relationship between User and Score Tables (priority | issue: #5)
- [x] isAdmin column in User table and Admin views (priority)
- [x] Notifications
- [x] Use Flask Blueprints
- [x] Finalize black theme?
- [x] Error messages not appearing in `/submit`
- [x] Implement `machine.html` to server a page where one can download/serve machines
