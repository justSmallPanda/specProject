from django.urls import path
from .views import *
urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('item/<slug:id>/', item, name='item'),
    path('items/', itemsPage, name='items'),
]