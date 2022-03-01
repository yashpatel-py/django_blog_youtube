from unicodedata import name
from django.urls import path
from authors import views

urlpatterns = [
    path('create-new-account/', views.signUp, name="register"),
    path('user-profile/<str:user_name>/', views.profile, name="profile"),
    path('login/', views.logIn, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('change_password', views.PasswordChangeView.as_view(template_name = "authors/password_change.html"), name="change-password"),
    path('password_success', views.password_success, name="password_success")
]
