from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/',include('food_app.urls')),
    path('users/',include('users.urls')),

]
