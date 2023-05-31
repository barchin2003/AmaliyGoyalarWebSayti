from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('<int:id>', idea_detail, name='detail')
]
