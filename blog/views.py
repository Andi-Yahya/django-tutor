from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'judul':'ini adalah blog',
        'subjudul':'ini adalah BLOG dari web django',
        'img':'blog/img/banner_blog.png',
    }

    # return render(request,"blog/blog.html",context) #ini untuk menunjukkan dimana lokasi templates, yang mana lokasinya saat ini adalah berada di sub folder templates yang bernama blog dan file didalamnya nya yaitu blog.html
    return render(request,"index.html",context) #menggunakan cara templating satu file sehingga key img akan terkirim ke file index umum di index pada templates

def recent(request):
    return render(request, "blog/recent.html") #ini untuk menunjukkan dimana lokasi templates, yang mana lokasinya saat ini adalah berada di sub folder templates yang bernama blog dan file didalamnya nya yaitu recent.html