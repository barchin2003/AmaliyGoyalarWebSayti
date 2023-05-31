Amaliy g'oyalar websayti

O'rnatish
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/barchin2003/AmaliyGoyalarWebSayti.git
$ cd /music_store
```
Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install pipenv
$ pipenv shell
```
Then install the dependencies:
``sh
(env)$ pip install django
(env)$ pip install Pillow
```
Once pip has finished downloading the dependencies:
```sh
(env)$ cd AmaliyGoyalarWebSayti/
(env)$ python manage.py runserver
```
```sh
And navigate to http://127.0.0.1:8000/.
```
