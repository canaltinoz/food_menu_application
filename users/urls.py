from django.urls import include, path
from users import views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='food_app/index.html'),name='logout'),
    path('profile/',views.profile,name='profile'),


]
