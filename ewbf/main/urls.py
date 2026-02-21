from django.urls import path
from ewbf.main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
]
