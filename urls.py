"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = ...
urlpatterns = staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path



from skydzygn.views import index
from skydzygn.views import about
from skydzygn.views import contact
from skydzygn.views import portfolio
from skydzygn.views import team

from login.views import login
from login.views import signup
from login.views import profile




urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', index, name ='home'),
    path('about', about, name ='about'),
    path('contact', contact, name ='contact'),
    path('portfolio', portfolio, name ='portfolio'),
    path('team', team, name ='team'),
    path('login', login, name ='login'),
    path('signup', signup, name ='signup'),
    path('profile', profile, name ='profile')

]
