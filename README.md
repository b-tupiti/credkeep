
# CredKeep

An app to keep all your credentials in one place. Its built for fun! 




## Prerequisites

Ensure you have python installed on your machine. 

Go to https://www.python.org/downloads/, download and install python.

Now, on to the good stuff!
### Download

Download the zip file, extract it, open the terminal, and navigate to the project root folder ( i.e. where manage.py file lives ).
### Environment Variables

Inside the config folder, create a .env file and paste this in ( or any random string would do).

`SECRET_KEY=+k%3sog56t#i15qub!fdnaq$l0pg$r$k1501ewry_`

Open your settings.py file and remove these lines.

`EMAIL_BACKEND = env('EMAIL_BACKEND')`

`EMAIL_HOST = env('EMAIL_HOST')`

`EMAIL_PORT = env('EMAIL_PORT')`

`EMAIL_USE_TLS = env('EMAIL_USE_TLS')`

`EMAIL_HOST_USER = env('EMAIL_HOST_USER')`

`EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')`




### How to setup locally

Create a virtual environment

```bash
  python -m venv venv
```

Activate your virtual environment
```bash
  venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Migrate to sqlite3 database

```bash
  python manage.py migrate
```

Create your superuser account (enter username and password of your choice)

```bash
  python manage.py createsuperuser
```

Serve the application

```bash
  python manage.py runserver
```


### Notes
 
This app  is in continuous development. 

However, at this stage, I think it might come in handy for the busy proffessional who either keeps forgetting his/her credentials, or has just too many he lost count. 

Feel free to obtain it and use it in your local environment. 


### Screenshot

![Home Page](https://github.com/dawnCoder26/credkeep/blob/main/static/images/readme/credkeep1.PNG)


### 🔗 Find me

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brandon-tupiti-75410012b/)

