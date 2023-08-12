from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:item_id>/',views.detail,name='detail'),
]
