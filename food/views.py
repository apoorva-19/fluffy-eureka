from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Item
from .forms import ItemForm

def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("<h1>This is an item view</h1>")

def detail(request, item_id):
    food_item = Item.objects.get(pk=item_id)
    context = {
        'food_item':food_item,
    }
    return render(request, 'food/detail.html', context)
    # return HttpResponse("This is item number: %s" % item_id)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item_form.html', {'form':form})

def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item_form.html', {'form':form, 'item':item})

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item_delete.html', {'item':item})