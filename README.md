# MarketPlace Api 

This api is the backend part of my marketplace project where the user can upload photos, descriptions, prices and categorize all the product that they want to sell.

The user is allowed to comment the product posted to show his interest, leave a like and follow the seller for don't miss any new product.

This database is developed using REST Framework.


# Database Structure

<img src='images/class_api.png'>



## Testing 

### Manual Testing

* CRUD Testing

- An authernticated user can succesfully update the own profile, read the list of profiles, delete the own profile, create a product insertion, read the list of product, update the own insertion, delete the own insertion

- An authenticated user can follow other profiles, unfollow the profiles, see the list of follower and follow

- An authenticated user can comment an insertion, delete his own comment, update it

- An authenticated user can leave like to one insertion, unlike the insertion

* Examples

- User can see the profile, have a delete button, can update changing the value in the form
<img src='images/profile-details.png'>

- User can create a product insertion

<img src='images/product-creation.png'>

- User can see product details, delete and update own insertions

<img src='images/product-details.png'>

- User can see follower list

<img src='images/follower-list.png'>

- User can delete(unfollow) 

<img src='images/follower-details.png'>

- User can see comment list
<img src='images/comment-list.png'>

-user can delete or update comment that own

<img src='images/comment-details.png'>







* Urls 

- Tested all the path to make sure everything work as expected 


<img src='images/urls.png'>


* Bugs

- At the moment I didn't occure any bug to be solved


# Project Creation

- Start your repository using the Code Institute gitpod-full-template

- Install the needed libraries, Django, after that start your project using the code django-admin startproject /nameofyourrepository/

- After that install django-cloudinary-storage and PIllow to use yhe credentials of your Cloudinary account.

- Add the app previously installed in settings.py

- Create an env.py file to set up your enviroment variables

- First of all import os in your env.py file and add the CLOUDINARY_URL variable with value of the url of your account

- Write an if stratement that check if env.py exists and if exists import env

- After that update settings.py adding the CLOUDINARY_STORAGE variable with CLOUDINARY_URL as an object with the value of the enviroment variable

- After that to create a new application in the project use the code python manage.py startapp /nameoftheapp/

- Update the installed app in settings.py

- For this project then is necessary to install djangorestframework


# Deployment

- Install JSON Web Tokens using the code pip install dj-rest-auth

- Update the settings.py file with the app just installed

- Include the urls from dj-rest-auth in the pattern list the urls using path('dj-rest-auth/', include('dj_rest_auth.urls'))

- Migrate the terminal with python manage.py migrate

- To allow the user to register install dj-rest-auth[with_social]

- Update the installed app with the required app just installed

- Add in settings.py the variable SITE_ID = 1 

- As for the dj-rest-auth include the urls using path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),

- Install the JSON tokens installing djangorestframework-simplejwt

- Before the deployment is required to define a DEV variable in env.py so in the settings.py is possible to define if the we are working in development or production

- The code used to define production or development is 

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],

- Add the code that enable token authentication 

- Create a serializer in the project folder to add the code for the current user 

- Replace the default user serializer in settings.py

- Migrate the database

- install dj_database_url==0.5.0 and psycopg2

- import dj_database_url in settings.py

- Update the Database variable adding the if statement that check for the presence of Dev variable to determine if we are in production or development

- Add in env.py the variable DATABASE_URL with the url of the ElephantSQL database create previously 

- To migrate all the data in the new database you need to comment out the DEV variable and then migrate all the database

- Create a new superuser from the moment the old one is not present anymore

- install Gunicorn

- Update ones again the requirements.txt file 

- Create a Procfile and add in it the command  release: python manage.py makemigrations && python manage.py migrate web: gunicorn /projectname/.wsgi 

- In settings.py replace the value of ALLOWED_HOST including the heroku app url 

- Add Corsheader in Middleware

- under the MiddleWare section add the code that check for the allowed origins that can make request to this api with the code  

    if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN')
     ]
    else:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
     ]
    CORS_ALLOW_CREDENTIALS = True

- Add the variable JWT_AUTH_SAMESITE

- replace the variable SECRET_KEY with the one in the enviromental file, if the secretkey used is expose in the gitpod commit make sure to change it before deploy on Heroku

- Set Debug on False

- update requirements.txt

- add, commit and push

- One done that go on Heroku and deploy the repository adding all the variable needed like CLOUDINARY_URL, DATABASE_URL, SECRET_KEY, DISABLECOLLECTSTATIC and ALLOWED_HOST


# CREDITS

- Big thanks to Code Institute for all the knowledge learn in this course and all the explaination step by step in this carrer change for me so important


