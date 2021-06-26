@echo off
echo %1
if %1==startenv C:\Users\USER\tutorial-py\Scripts\activate
if %1 == app django-admin startapp %2
if %1 == go python manage.py runserver %2
