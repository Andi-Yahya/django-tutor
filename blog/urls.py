# from django.conf.urls import path #django 1.1Lts
from django.urls import path #django 4.0


from . import views 

urlpatterns =[
    path("recent/",views.recent), #TIPS pastikan pada saat routing ke sub-url dari app alamat yang dituju di chrome harus sama agar tidak terjadi error dengan cara mengisi path sub-url nya seperti pada sub-url ini = path("recent/"..
    #url patterns untuk recent ini harus dibuat seperti ini karena melanjutkan url dari app utama yaitu django_project
    path("",views.index),
    path("recent/url",views.recent),
]


