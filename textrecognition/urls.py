"""textrecognition URL Configuration
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mainpage.views import home_view, processing, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('processing/<uuid:uuid>', processing, name = 'processing'),
    path('404', handler404),
    path('500', handler500),
    # path('image/<uuid:uuid>', image, name = 'image'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()