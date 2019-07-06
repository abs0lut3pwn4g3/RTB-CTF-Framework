# RootTheBox CTF Framework

A CTF framework(in flask) for HackTheBox style machines. 

## Features

* User Registration
* Hash submission (currently 2 hashes: user and root)
* Real time scoreboard tracking
* A page to show relevant details about the machine such as name, IP, OS, points and difficulty level. 

## To-do

- [ ] Password reset functionality
- [ ] admin views
- [ ] Support for more hashes
- [ ] More info for `home.html`
- [ ] Need to implement `account.html` (not a priority)
<hr/>

- [x] Finalize black theme?
- [x] Error messages not appearing in `/submit`
- [x] Implement `machine.html` to server a page where one can download/serve machines
- [x] Add basic info and stuff to `layout.html`
- [x] Login/logout/registration works fine.
- [x] User is able to submit hash multiple times and keep increasing score, so need to implement limitations
