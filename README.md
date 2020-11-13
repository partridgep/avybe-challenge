# Avybe Challenge

A Django app that lets logged-in users set and change a nickname and a profile picture.

## Getting Started

To view the deployed project, visit [this link](https://pp-avybe.herokuapp.com/) (please allow 20-30 seconds for Heroku to load.)

Alernatively, if you wish to run this app locally, open a terminal, navigate to the project's folder and open the project by typing `python3 manage.py runserver`.

*NOTE: If you open the app locally, you will not have access to my AWS config variables (due to security concerns), so you will not be able to add, view, or modify the pictures which are stored in an S3 bucket. You may modify the bucket settings in `views.py` if you wish.*

## List of Technologies

* Django
* Python
* PostgreSQL
* AWS S3 Storage
* HTML5
* CSS3
* JavaScript


## Screenshots 

![App homepage](https://i.imgur.com/oN64xT3.png)

## Functioning

`main.app` contains most of the actual code, including the `models.py`, `urls.py`, `views.py`, `forms.py`, as well as the `templates` folder.

### Models

There are two models inside of `models.py`, as we are using `User` from the default `django.contrib.auth.models`:

* `Profile`: a profile of extra components we are attaching to the `User` model. In this case, just a `nickname`. This is a one-to-one relationship to the `User`.
* `Picture`: a url string to the image stored in the AWS S3 bucket. This is a one-to-one relationship to the `User`.

### Views

There is a mix of function-based views and class-based views in `views.py`.

The function-based views relate to the homepage and signup page, as well as the picture upload functionalities.

For more simplicity, class-based views are utilized for adding and modifying nicknames, accessing the same Django form for the model.
