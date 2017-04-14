This is an updated version of Simple CRUD django application with MPTT-Model available in https://github.com/kaygorodov/simple-crud-mptt
that allows to test the concepts of MPTT contained in https://github.com/django-mptt/django-mptt/tree/ and documented in https://django-mptt.github.io/django-mptt/index.html

Additional description of the application is available in http://stackoverflow.com/questions/11508088/django-how-to-do-crud-with-django-mptt

There are some changes in the database to include additional fields to be used in a skill management tool using django framework, with the default sqlite database

In order to make it working you need to set the database using the following steps:


python manage.py makemigrations genre

python manage.py migrate

python manage.py runserver
