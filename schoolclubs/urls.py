"""schoolclubs URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from pupils.views import get_homepage, get_admin_page, get_manage_booking
from pupils.views import get_make_booking, add_pupil
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pupils import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_homepage, name='home'),
    path('accounts/', include('allauth.urls')),
    path('admin_page/', get_admin_page, name='admin_page'),
    path('manage_bookings/', get_manage_booking, name='get_manage_booking'),
    path('book_new/', get_make_booking, name='new_booking'),
    # path('add_pupil/', views.add_pupil, name='add_pupil'),
    path('add_pupil/', views.AddPupil.as_view(), name='add_pupil2'),
]
urlpatterns += staticfiles_urlpatterns()
