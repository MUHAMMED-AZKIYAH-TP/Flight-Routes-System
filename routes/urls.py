# routes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_route, name="add-route"),
    path("nth/", views.nth_node, name="nth-node"),
    path("longest/", views.longest_route, name="longest"),
    path("shortest/", views.shortest_route, name="shortest"),
]
