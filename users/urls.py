from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('edit-account/', views.editUserAccount, name="edit-user-account"),
    path('signup/', views.signUp, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('delete-account/', views.deleteUserAccount, name="delete-account"),

    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="users/change_password.html"),name="change-password"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),name="password_change_done"),
]