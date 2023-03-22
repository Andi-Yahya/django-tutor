from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'judul':'ini adalah blog',
        'subjudul':'ini adalah BLOG dari web django',
        'img':'blog/img/banner_blog.png',
        'app_css':'blog/css/styles.css',
    }

    # return render(request,"blog/blog.html",context) #ini untuk menunjukkan dimana lokasi templates, yang mana lokasinya saat ini adalah berada di sub folder templates yang bernama blog dan file didalamnya nya yaitu blog.html
    return render(request,"index.html",context) #menggunakan cara templating satu file sehingga key img akan terkirim ke file index umum di index pada templates

def recent(request):
    context = {
        'judul':'ini adalah Recent',
        'subjudul':'ini adalah Recent dari Blog web django',
        'app_css2':'blog/css/styles2.css', #ini adalah cara untuk menggunakan static, sehingga pada file yang dituju hanya memerlukan variabelnya saja
    }
    return render(request, "index.html",context) #ini untuk menunjukkan dimana lokasi templates, yang mana lokasinya saat ini adalah berada di sub folder templates yang bernama blog dan file didalamnya nya yaitu recent.html