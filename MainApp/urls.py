from django.urls import path
from .views import *

urlpatterns = [ 
    path('', index),
    path("<str:url_slug>/", redirection)
]