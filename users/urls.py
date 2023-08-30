from django.urls import include, path
from users import views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='food_app/index.html'),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile-update/',views.profile_update,name='profile-update'),
]
urlpatterns +=[] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
