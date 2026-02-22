from django.urls import path
from ewbf.people import views

urlpatterns = [
    path("", views.add, name="add"),
    # path("contact", views.contact, name="contact"),
]
