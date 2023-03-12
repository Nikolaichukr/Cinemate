# Cinemate

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Build Status](https://app.travis-ci.com/Nikolaichukr/Cinemate.svg?branch=main)](https://app.travis-ci.com/Nikolaichukr/Cinemate)
[![Coverage Status](https://coveralls.io/repos/github/Nikolaichukr/Cinemate/badge.svg?branch=main)](https://coveralls.io/github/Nikolaichukr/Cinemate?branch=main)

## What is it?

Cinemate is a Flask CRUD application that enables users to manage movies and reviews for those movies. It is a simple
and intuitive application perfect for movie enthusiasts who want to keep track of their favorite movies and share their
thoughts and reviews with friends.

I built this app to demonstrate my skills and knowledge in web development. It provides both a web interface and a
RESTful API.

## Features

* View movies and corresponding reviews;
* Filter movies by year;
* Add new movies to the database;
* Edit and delete existing movies;
* Add reviews for movies;
* Edit and delete reviews.

## Technologies

Cinemate is built using the following main technologies:

* Python
* Flask framework
* MySQL database

## Installation

### Prerequisites

Before running the Cinemate app, make sure you have the following software installed:

- Python 3
- pip
- venv
- MySQL

For Debian-based distros that use Advanced Packaging Tool (APT), you can use the following commands to install the
prerequisites:

```
sudo apt update
sudo apt install python3 python3-pip python3-venv mysql-server mysql-client
```

### MySQL Setup

Once MySQL is installed, you will need to create a new database and user for Cinemate. Follow the steps below.

1. Log in to MySQL using the following command (the default password is blank, just hit Enter):

   ```
   sudo mysql -u root -p
   ```

2. Create a new user named `cinemate-user` with password `cinemate-password`, and a new database named `Cinemate`. Use
   the following commands:

   ```
   CREATE USER 'cinemate-user'@'localhost' IDENTIFIED BY 'cinemate-password';
   GRANT ALL PRIVILEGES ON *.* TO 'cinemate-user'@'localhost';
   FLUSH PRIVILEGES;
   
   CREATE DATABASE Cinemate;
   ```

3. Once you have created the user and database, exit MySQL using the following command:

   ```
   exit;
   ```

### Running the Cinemate App

Once you have installed the prerequisites and set up MySQL, you can run the Cinemate app by following these steps:

1. Clone the Cinemate repository using the following command:

   ```
   git clone https://github.com/Nikolaichukr/Cinemate
   ```

2. Navigate to the Cinemate directory using the following command:

   ```
   cd Cinemate
   ```

3. Create a new virtual environment for the app using the following command:
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment using the following command:

   ```
   source venv/bin/activate
   ```

5. Install the required Python packages using the following command:

   ```
   pip install -r requirements.txt
   ```

6. Create `.env` file with the following variables:

   ```
   MYSQL_USER=cinemate-user
   MYSQL_PASSWORD=cinemate-password
   MYSQL_SERVER=127.0.0.1:3306
   MYSQL_DATABASE=Cinemate
   ```

7. If necessary, initialize and create migrations using the following commands:

   ```
   flask db init
   flask db migrate
   ```

   Otherwise, execute the following command to upgrade existing migrations:

   ```
   flask db upgrade
   ```

8. Populate the database with some data using the following command:

   ```
   python -m cinemate_app.service.populate_database
   ```

9. Finally, start the app using the following command:

   ```
   gunicorn cinemate_app:app
   ```

The Cinemate app should now be running at `http://127.0.0.1:8000`.

