# /src/ Structure 

    /src/static/ --> contains css
    /src/templates/ --> templates for rendering the html
    /src/fitness_app.py --> does all of the main set up for logging in, database creation, etc. 
    /src/run.py --> runs the main function (basically you can just do python3 run.py to start everything up)
    /src/models.py --> holds database information
    /src/views.py --> holds the routing information for different views


# Setting up Flask 

## 1. Installing Flask

    pip3 install flask

## 2. Activating Virtual Environment 

    a. pip3 install virtualenv
    b. Create virtual environment with command: *virtualenv "name"*
    c. Run virtual environment with command: *source "name"/bin/activate*
    d. To deactivate, use command: *deactivate*

    allows you to maintain certain packages within the virtual environment without worrying about accidentally updating sources 

## 3. Running Application 

    a. Define the main program (ex: app.py)
    b. export FLASK_APP=fitness_app and FLASK_ENV=development (for dev mode, catching errors)
    c. flask run -- runs local host (for now)
        c.1. LATER: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html 

# Flask Resources

https://flask.palletsprojects.com/en/2.3.x/ 

https://www.fullstackpython.com/flask.html

https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/

https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3
