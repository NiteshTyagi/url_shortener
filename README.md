# Django URL Shortening App
This module allows you to create short and simple readable url from a very long url.

## Steps to run this project.
**1. First Clone this repo into your local system.**

```bash
git clone https://github.com/NiteshTyagi/url_shortener.git
```

**2. Then after cloning, open terminal and navigate to the url_shortener folder into local system.**

**3. Install the required python library which needs to run this application properly.**

```bash
pip install -r requirements.txt
```

**4. Then Run the following commands:**

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

**5. Create a superuser to login into django-admin panel (/admin)**

```bash
python3 manage.py createsuperuser
```

**8. Go to url_shortener/settings.py file and edit the DOMAIN_NAME parameter to the domain where your application is being hoisted.**

**7. Last step: Run the Django server on 8080 because this port is used in test cases**

```bash
python3 manage.py runserver
```

**8. If everything works as expected, then Open the browser and run the <domain>/admin URL or go to <domain>/v1/post for generating the short URL[s].**