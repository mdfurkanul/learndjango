from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    data = {
        'name':"md",
        "ages":[25,36,15,45]
            }
    return render(request,"home.html",data)

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html",{})

def about_view(request, *args, **kwargs):
    return render(request,"about.html",{})
