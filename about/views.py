from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"about.html")  #pastikan tanda petik harus sama dengan tanda petik yang ada di library urls bagian urlPatterns
