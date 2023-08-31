from django.shortcuts import render,redirect
from .models import Item
from .forms import ItemForm


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

def add(request):
    if request.method == 'POST':
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    form=ItemForm()
    return render(request,'food_app/add.html',{'form':form})

def update(request,item_id):
    if request.method == 'POST':
        item=Item.objects.get(pk=item_id)
        form=ItemForm(request.POST or None,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('list')
        
    item=Item.objects.get(pk=item_id)
    form=ItemForm(instance=item)   
    return render(request,'food_app/update.html',{'form':form,'item':item})
