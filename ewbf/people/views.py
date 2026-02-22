from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    return render(request, "add.html")


# def contact(request):
#     return render(request, "contact.html")
