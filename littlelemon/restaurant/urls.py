from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
from .views import index
from . import views
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    #path('', sayHello, name='sayHello'), 
    path('', index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]