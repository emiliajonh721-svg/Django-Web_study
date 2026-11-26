"""
URL configuration for enclub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.homepage),
    path('homepage',views.Home, name='Homepage'),
    path('allcourse/',views.Allcourse,name='Allcourse'),
    path('allcourse/ElectronicBooks/',views.ElectronicBookspage,name='ElectronicBooks'),
    path('Beginers/',views.Beginers,name='Beginers'),
    path('Intermediate/',views.Intermedait,name='Intermediate'),
    path('Advance/',views.Advance,name='Advance'),
    path('IELS/',views.IELS,name='IELS'),
    path('TourGuides/',views.TourGuide,name='TourGuides'),
    path('EnglishTech/',views.Tech,name='EnglishTech'),
    path('EnglishPolotics/',views.Politic,name='EnglishPolotics'),
    path('EnglishBussiness/',views.Bussiness,name='EnglishBussiness'),
    path('Contact/',views.Contact,name='Contactus'),
    path('aboutus/',views.Aboutus,name='aboutus'),
    path('',views.login_view,name='loginform')
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.login_view, name='login'),
    path('homepage/', views.Home, name='Homepage'),
    path('allcourse/', views.Allcourse, name='Allcourse'),
    path('allcourse/ElectronicBooks/',views.ElectronicBookspage,name='ElectronicBooks'),
    path('Beginers/',views.Beginers,name='Beginers'),
    path('Intermediate/',views.Intermedait,name='Intermediate'),
    path('Advance/',views.Advance,name='Advance'),
    path('IELS/',views.IELS,name='IELS'),
    path('TourGuides/',views.TourGuide,name='TourGuides'),
    path('EnglishTech/',views.Tech,name='EnglishTech'),
    path('EnglishPolotics/',views.Politic,name='EnglishPolotics'),
    path('EnglishBussiness/',views.Bussiness,name='EnglishBussiness'),
    path('Contact/',views.Contact,name='Contactus'),
    path('aboutus/',views.Aboutus,name='aboutus'),
    path('',views.login_view,name='loginform')
]



