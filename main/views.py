from django.shortcuts import render
# from django.http import HttpResponse
from .models import items,contact

# Create your views here.
def index(request):
    Items = items.objects.all()
    context = {
        'items' : Items
    }
    return render(request, 'main/index.html',context)

