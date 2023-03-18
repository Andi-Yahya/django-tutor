from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"blog/blog.html") #ini untuk menunjukkan dimana lokasi templates, yang mana lokasinya saat ini adalah berada di sub folder templates yang bernama blog dan file didalamnya nya yaitu blog.html

def recent(request):
    return render(request, "blog/recent.html") #ini untuk menunjukkan dimana lokasi templates, yang mana lokasinya saat ini adalah berada di sub folder templates yang bernama blog dan file didalamnya nya yaitu recent.html