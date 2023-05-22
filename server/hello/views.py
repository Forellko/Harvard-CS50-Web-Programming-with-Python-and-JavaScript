from django.shortcuts import render

# Create your views here.

def greet(request, name):
    return render(request, "hello/index.html", {
        "name": name
    })