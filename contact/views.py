from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nama':'Andi',
        'bahasa':'Python',
        'kota': 'Bandung Kota',
        'nav': [
            ['..','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ]
    }
    return render(request,'contact/contact.html',context)