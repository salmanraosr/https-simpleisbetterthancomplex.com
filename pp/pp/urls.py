from django.contrib import admin
from django.urls import path
from ppapp.views import sendanemail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sendanemail,name="email")
]