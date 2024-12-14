from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
from django import forms
import random
class NewPageForm(forms.Form):
       title = forms.CharField(max_length = 100, label="Title")
       content = forms.CharField(widget=forms.Textarea)

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
     
def new_page(request):
        if request.method == "POST":
               form = NewPageForm(request.POST)        
               if form.is_valid():
                      title = form.cleaned_data["title"]
                      content = form.cleaned_data["content"]
                      util.save_entry(title,content)
                      return  HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            form = NewPageForm()
            return render(request,"encyclopedia/newpage.html",{"form":form})
def random_page(request):
       entry = random.choice(util.list_entries())
       content = util.get_entry(entry)
       context = {"title":content}
       return render(request,"detail/detail.html",context)