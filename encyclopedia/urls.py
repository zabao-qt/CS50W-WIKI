from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.view_entry, name="view_entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("edit/<str:entry>", views.edit, name="edit"),
    path("random/", views.random_entry, name="random_entry"),
]
