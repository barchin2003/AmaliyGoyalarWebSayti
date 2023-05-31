Amaliy g'oyalar websayti

O'rnatish
The first thing to do is to clone the repository:

$ git clone https://github.com/barchin2003/AmaliyGoyalarWebSayti.git
$ cd /music_store
Create a virtual environment to install dependencies in and activate it:

$ pip install pipenv
$ pipenv shell
Then install the dependencies:

(env)$ pip install -r requirements.txt
Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/.