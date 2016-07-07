Material design for Django v1.8+ on OpenShift
=============================================

This is a small project to helps you get up and running quickly with Material Design for django v1.8+ and Openshift.

Include the following libraries
===============================

 * Django==1.8.2
 * django-material==0.7.0

Usage
=====
- Create an account at https://www.openshift.com
- Install the RHC client tools if you have not already done so.
```
sudo gem install rhc
rhc setup
```
- Create a Python 2.7 application
```
rhc app create app-django python-2.7
```
- Add the database cartridge (choose one)
```
rhc add-cartridge postgresql-9.2 --app app-django

OR

rhc add-cartridge mysql-5.5 --app app-django 
```
- Add this upstream repo
```
cd app-django
git remote add upstream -m master https://github.com/JohnProg/django-material-openshift.git
git pull -s recursive -X theirs upstream master
```
- set the WSGI application to django's built in WSGI application (stored in the wsgi folder).
```
rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=wsgi/wsgi.py --app app-django
```
- Push the repo upstream
```
git push
```
- SSH into the application to create a django superuser.
```
python app-root/repo/manage.py createsuperuser
```
- Now use your browser to connect to the Admin site.
