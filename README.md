## Configuring the Database

You will be using an SQLite database. You could create an SQLite database on your own, but let’s have Flask-SQLAlchemy do it for you. You already have the path of the database specified in the __init __.py file, so you will need to tell Flask-SQLAlchemy to create the database in the Python REPL.

Ensure that you are still in the virtual environment and in the flask_auth_app directory.

If you stop your app and open up a Python REPL, you can create the database using the create_all method on the db object:

``` py
>>> from project import db, create_app, models
>>> db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
```
