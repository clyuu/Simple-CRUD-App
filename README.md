# Simple CRUD App

A simple CRUD application using Tkinter and MySQL.

## Description

This application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on a MySQL database. It uses the Tkinter library for the graphical user interface and the MySQL Connector for database interactions.

## Features

- Add new records to the database.
- Display all records in a Treeview.
- Update existing records.
- Delete records.

## Requirements

- Python 3.x
- Tkinter
- mysql-connector-python

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/simple-crud-app.git
    cd simple-crud-app
    ```

2. Install the required packages:
    ```sh
    pip install mysql-connector-python
    ```

3. Set up your MySQL database and update the `connect_db` function in `crud_app.py` with your database credentials.

## Usage

Run the application:
```sh
python crud_app.py
