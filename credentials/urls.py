from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', views.accounts, name="accounts"),
    path('account/<str:pk>/', views.account, name='account'),
    path('create-account/', views.createAccount, name='create-account'),
    path('edit-account/<str:pk>/', views.editAccount, name='edit-account'),
    path('delete-account/<str:pk>/', views.deleteAccount, name='delete-account'),
]