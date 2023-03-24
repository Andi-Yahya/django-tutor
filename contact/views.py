from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul':'ini adalah contact',
        'subjudul':'ini adalah kontak',
        'app_css3':'contact/css/styles.css',
        'nav': [
            ['..','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ],
    }
    return render(request,'index.html',context)