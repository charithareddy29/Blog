from django.urls import path#importing the paths
from . import views# here dot represents that it is importing the views module from current page
#url patterns is a list that consists of the base url appliation('')
urlpatterns=[
    path('',views.index,name='index')
]