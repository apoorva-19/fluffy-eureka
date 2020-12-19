from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

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
