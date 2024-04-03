"""
URL configuration for customer_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .api import create_customer
from django.urls import include, path
from .api import create_customer, create_quote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/create_customer/', create_customer),
    path('customer/', include('customer_backend.urls')),       
    path('api/v1/create_customer/', create_customer, name='create_customer'),
    path('api/v1/quote/', create_quote, name='create_quote'),
]
from django.urls import path
from .api import create_customer, create_quote, search_customers, search_policies

urlpatterns = [
    path('api/v1/create_customer/', create_customer, name='create_customer'),
    path('api/v1/quote/', create_quote, name='create_quote'),
    path('api/v1/search_customers/', search_customers, name='search_customers'),
    path('api/v1/search_policies/', search_policies, name='search_policies'),
]