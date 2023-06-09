from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nama':'Andi Yahya',
        'jurusan':'Teknik Informatika',
        'subjudul': 'I LOVE DJango so Much from now on, need to knuckle down on it',  
        'img':'about/img/banner_about.png',
        'app_css':'about/css/style.css',
    }
    # return render(request,"about.index.html",context)  #pastikan tanda petik harus sama dengan tanda petik yang ada di library urls bagian urlPatterns di dalam parameter dari  Include() nya
    return render(request,"index.html",context) #menggunakan cara templating satu file sehingga key img akan terkirim ke file index umum di index pada templates


def me(request):
    context = {
        'nama':'Ucup Siregar',
        'jurusan':'Sistem Tatanan DPR'
    }
    return render(request,'about/index.html',context)
