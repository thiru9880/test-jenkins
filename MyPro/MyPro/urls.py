"""MyPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from Students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('add_details/', views.add_details),
    path('add_student/', views.add_student),
    path('add_education/', views.add_education),
    path('add_govtId/', views.add_govtId),
    path('add_consultancy/', views.add_consultancy),
    path('add_communication/', views.add_communication),
    path('dump_to_csv/', views.dump_to_csv),
    path('load_from_csv/', views.load_from_csv),
    path('drop_all_tables/', views.drop_all_tables),
    path('show_students/',views.show_students),
    path('search_mail/',views.search_mail),
]
