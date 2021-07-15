# Installation / How To Use

### Requirements

* Tested on `Python 3.8.3`
* Python Packages: [`src/requirements.txt`](src/requirements.txt).
* OS Packages: PostgreSQL version 11 or greater, `libpq-dev`, `python3-dev` packages. Please refer [here](https://tutorials.technology/solved_errors/9-Error-pg_config-executable-not-found.html).

### Build locally and run (Development)

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

3. With `virtual environment` activated, install requirements, init db,

```bash
[venv]$ pip install -r requirements.txt
[venv]$ export FLASK_APP="FlaskRTBCTF:create_app()"
[venv]$ chmod +x init_db.sh && ./init_db.sh # Only required on first run
```

4. Now we can run our application,

    - For development server,

    ```bash
    [venv]$ python run.py 
    ```

    - Production server

    ```bash
    [venv]$ ./runserver.sh
    ```

### Docker (Production)

1. You need `docker` and `docker-compose` installed on your host machine. (refer [here](https://docs.docker.com/engine/install/) and [here](https://docs.docker.com/compose/install/))

2. Define certain environment variables present in files `.env` and `.env_postgres`.

3. After having configured these environment variables, just execute,

    ```bash
    $ docker-compose up
    ```
