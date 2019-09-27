# Ajust Task (Django HTTP API Endpoint)

## Requirements
- Django 
- Django Rest Framework
- MySQL

```
pip install -r requirements.txt
```
use this command to install the requirements for this project.

## Create DB
1. To create DB, change the USER and PASSWORD fields in the settings.py file (located at: AdjustTask ->  task -> task -> settings.py)  
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'performance_metric',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```
2. Use the script adjust.sql to create the Database. Then run the following migrations to create table in the Database.

```
python manage.py makemigrations dataset
python manage.py migrate
```

At this point, your tables should have been created in the DB. 

## Run and Start Application

Use this command to start the application. 

```
python manage.py runserver
```
The application will be running on http://127.0.0.1:8000/dataset . Displaying a Welcome Message. 

1. Read and Load the CSV data into DB using http://127.0.0.1:8000/dataset/load_data URL. 


To see the Results of Use Cases:

2. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, 
sorted by clicks in descending order. Use ```http://127.0.0.1:8000/dataset/get_data?attrs=impressions``` URL

3. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
Use http://127.0.0.1:8000/dataset/get_data?attrs=installs URL

4. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
Use http://127.0.0.1:8000/dataset/get_data?attrs=revenue URL

5. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. 
Use http://127.0.0.1:8000/dataset/get_data?attrs=cpi URL
