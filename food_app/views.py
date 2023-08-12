from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Item


def index(request):
    return render(request,'food_app/index.html')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    return render(request,'food_app/detail.html',{'item':item})

def list(request):
    item=Item.objects.all()
    return render(request,'food_app/list.html',{'item':item})

def delete(request,item_id):
    item=Item.objects.get(pk=item_id)
    item.delete()
    return redirect('list')