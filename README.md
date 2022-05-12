# Carbon Footprint Database
--
The goal of this is to convey carbon footprint in a very human digestible manner. 
e.g. 3 hr of airplane flight = 20 burgers. 
The goal is to convey the scale rather than exact numerical value. 


# Clone this repo
--
In case, this pops up while pushing changes to git: "remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
", follow this link:

https://stackoverflow.com/questions/68775869/support-for-password-authentication-was-removed-please-use-a-personal-access-to


# To run locally using docker


1) docker-compose up web


# To run locally using venv


1) Follow this if you are not familiar with venv: https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b
2) create a new venv (lets call it venv)
3) activate the virtual environment (. venv/bin/activate in this scenario)
4) pip install -r requirements.txt 
5) python manage.py migrate 
6) python manage.py runserver 







