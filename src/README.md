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
    b. export FLASK_APP=app or FLASK_APP=development (for dev mode, catching errors)
    c. flask run -- runs local host (for now)
        c.1. LATER: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html 

