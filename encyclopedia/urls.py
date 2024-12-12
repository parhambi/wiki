from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/",views.detail,name="detail"),
    path("wiki/search",views.search,name="search"),
    path("wiki/createNewPage",views.CreateNewPage,name="NewPage")
]
