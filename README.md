# LittleLemonCapstone

This is the Little Lemon Capstone Project.

# To set up project environment

* Create a folder to store the capstone project
* cd into this folder
* Use git clone command to clone remote repository to your local machine
* Open the project in VS Code
* Open VS Code terminal
* cd LittleLemonCapstone
* python3 -m venv myenv
* source myenv/bin/activate
* pip3 install django
* pip3 install mysqlclient
* pip3 install djangorestframework
* pip3 install djoser
* cd littlelemon
* start mysql server
* python3 manage.py runserver

# MySQL

* !!! IMPORTANT !!!

* Make sure to enter the right 'USER' and 'PASSWORD' in the DATABASES section in the settings.py file.

* Make sure to start your MySQL server before starting the server.

* Don't forget to use python3 manage.py makemigrations and python3 manage.py migrate

1. Open VSCode terminal
    * Type: mysql - u root -p
    * Enter your mysql password.
    * Type: SHOW DATABASES;
    * Note: a database named littlelemon should be present.  If there is none, use CREATE DATABASE littlelemon;
    * Type: SHOW DATABASES;
    * Type: USE littlelemon;
    * Type: SHOW TABLES;
    * Type: SELECT * FROM restaurant_booking;
    * Type: SELECT * FROM restaurant_menu;

# User information

1. Admin
   * Username
     + admin
   * Password
     + password
   * Authentication Token
     + 0a1cb704e3ffb1e09dae8c5d5a41c438e5bf75fd

2. Mario
   * Username
     + mario
   * Password
     + mario@123!
   * Authentication Token
     + c81e631a2f0d880d0d57cb28d8699ec89c2e352a

2. Adrian
   * Username
     + adrian
   * Password
     + little@123!
   * Authentication Token
     + 3f876b6b57bc1f13fe2826e6373271f5a64879d3

# API endpoints

* GET request with Bearer token 
    + To retrieve menu items
        * http://127.0.0.1:8000/restaurant/menu

    + To add a menu item using a POST request
    + Note the / at the end of the url path.
        * http://127.0.0.1:8000/restaurant/menu/
            + JSON
                + Example:
                * {
	                "title": "Burger",
	                "price": "9.00"
                }

    + To GET, PUT, DELETE a single menu item with bearer token
        * http://127.0.0.1:8000/restaurant/menu/1
            + JSON
                + Example:
                * {
	                "title": "Burger",
	                "price": “10.00"
                    }

    + To GET or retrieve booking information with bearer token
    + Note the / at the end of the url path.

        * http://127.0.0.1:8000/restaurant/booking/tables/

    + To POST or create a booking reserveation with bearer token using Insomnia
    + Note the / at the end of the url path.

        * http://127.0.0.1:8000/restaurant/booking/tables/
            + Example:
            + {
		        "name": "Adrian",
		        "number_of_guests": 7,
		        "booking_date": "2024-06-14T18:00:00Z"
                }

    + To create a new user with a POST request
    + Note the / at the end of the url path.

        * http://127.0.0.1:8000/auth/users/
            + Enter email, username, and password
            + Example:
            + {
                "email": "john@littlelemon.com",
                "username": "john",
                "password": "lemon@123!"
                }

    + To create user token
        * http://127.0.0.1:8000/auth/token/login
            + Enter username and password and use POST request
            + Example:
            + {
	            "username": "adrian",
	            "password": "little@123!"
                }

    + To view auth token from a user using a POST request
    + Note the / at the end of the url path. Use Insomnia.

        * http://127.0.0.1:8000/restaurant/api-token-auth/
            + Enter username and password
            + Example: 
            + {
	            "username": "admin",
	            "password": "password"
                }

    + To remove auth token from user use a POST request and enter the Bearer Token
    + Note the / at the end of the url path.

        * http://127.0.0.1:8000/auth/token/logout/
            + Use POST request