from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


def index(request):
    item=Item.objects.all()
    return render(request,'food_app/index.html',{'item':item})

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    return render(request,'food_app/detail.html',{'item':item})