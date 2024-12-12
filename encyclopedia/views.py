from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def detail(request,title):
            title = util.get_entry(title)
            context = {"title":title}
            return render(request,"detail/detail.html",context)
def search(request):
     if request.method == "GET":
          page = request.GET.get("title")
          title = util.get_entry(page)
          context = {"title":title}
          return render(request,"detail/detail.html",context)