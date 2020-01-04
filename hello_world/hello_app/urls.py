from django.urls import path
from . import views

# a list of all urls supported by this app
urlpatterns = [
    path('',views.index)  #views.index is the name of the function inside the views file
]



