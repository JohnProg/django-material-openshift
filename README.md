Material design for Django v1.8+ on OpenShift
=============================================

This is a small project to helps you get up and running quickly with Material Design for django v1.8+ and Openshift.

Include the following libraries
===============================

 * Django==1.8.2
 * django-material==0.7.0

Usage
=====

Clone this repository and use like base of your Django project.

Set the following:
rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=wsgi/wsgi.py --app <app-name>
