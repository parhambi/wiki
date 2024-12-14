from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/",views.detail,name="detail"),
    path("wiki/search",views.search,name="search"),
    path("createnewpage/",views.new_page,name="newpage"),
    path("random/",views.random_page,name="random"),
    path("wiki/edit/<str:title>/",views.edit_page,name="edit")
]
