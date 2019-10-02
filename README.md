# Blog_Structure

This repo contains the basic blog structure for the website


**Changes to be made in your project file to make django_blog_it working**

Clone the repo and execute the requirements.txt to resolve system dependencies

  * pip install -r requirements.txt
  
Now follow the steps to make your project working:

eg, if your project name is 'Db_Proj' the, the project structure is like:

      Db_proj
          -Db_Proj
              -urls.py
              -settings.py
              ...
          -manage.py
          ...

1. Add app name in settings.py(in Db_proj)::

    INSTALLED_APPS = [
    
       '..................',
       'simple_pagination',
       'django_blog_it.django_blog_it',
       '..................'
    ]

2. Include the django_blog_it urls in your urls.py(in Db_Proj)::

    from django.conf.urls import include

    urlpatterns = [
    
        url('admin/', admin.site.urls),
        url('', include('django_blog_it.urls')),
    ]

now migrate the changes and run your server

You are good to go!!
