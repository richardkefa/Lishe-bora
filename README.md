# BlogPost
#### By Lourine Millicent
## Description
 A personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users. 

## User Stories
* As a user, I would like to view the blog posts on the site
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to an email alert when a new post is made by joining a subscription.
* As a user, I would like to see random quotes on the site
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.

## Technologies Used
  * Python 3.8
  * HTML5, CSS and Bootstrap
  * Flask Framework
  * Postgressql
  * Heroku

## BDD
Given a user inputs there credentials, when said user logs in he/she should be able to create and share their opinions/posts and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users. 
>Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg wangari``|
| Password  | Account password, ``eg pass1234``|

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg wangari``|
| Email  | User email, ``eg wangari@gmail.com``|
| Password  | Account password, ``eg pass1234``|
| Confirm Password  | Account password, ``eg pass1234``|

> Blog Post inputs

| Inputs | Description  |
|---|---|
|  Blog Post | The actual blog post body|
| Comment| A comment on the post|


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/Lourine/Pitch-App.git

        $ cd Pitch-App

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.8 -m pip install Flask
        $ python3.8 -m pip install Flask-Bootstrap
        $ python3.8 -m pip install Flask-Script
        $ python3.8 -m pip install Flask-Login
        


* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py tests


Open the application on your browser `127.0.0.1:5000`.

## Contact Information 

If you have any question or contributions, please email me at [lourine.millicent@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2020 **Lourine Millicent**
