from django.shortcuts import render
from django.http import HttpResponse
from .models import Person


def add(request):
    profile = Person.objects.all()
    
    return render(request, "add.html", {'profile': profile})


# def contact(request):
#     return render(request, "contact.html", {)
