# Flask APP template

A template/skeleton for a python application that has user authentication and flask blueprints (to modularize the program i.e., to implement design patterns)

The database will be created automatically the first time you run the run.py file

the dash directory has the files that defines routes for the dashboard (like index), and ther auth directory defines routes related to user authentication.

The Front-end design has used bootstrap for basic components like the navbar. As currently implemented templates extend the base html file.

classes that inheret db.model use objects of that class to represent query results, and values to be added to a database, found in app/models.

The imports.py file has imported many modules that I have found useful for making flask-apps. Many can be removed depending on the project, however.