"""Owo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myap import views
from myap.chater import oWo_
from myap import auOp 
urlpatterns = [
    path('admin/', admin.site.urls),
]
chater = views.CHAT()
owo = oWo_()
urlpatterns += [
    #path('',views.home),
    path('test/',views.t,name='test'),
    path('jstest/',views.jst,name='jstest'),
    #path('',views.load_chat_html),
    path('Gotalking/',owo.start,name='start'),
    path('talking/',owo.talking,name='talking'),
    path('noteSAVE/',owo.noteSAVE,name='noteSAVE'),
    path('todosubmit/',chater.todosubmit),
    #path('sign_up/', auOp.SignUpView.as_view(), name = "sign_up"),
    path('', views.login, name = "login"),
    path('ajaxt/',views.ajaxt, name='ajaxt'),
    path('getNotes/',views.getNotes,name='getNotes'),
    path('getTodos/',views.getTodos,name="getTodos")
    path('saveNotes/',views.saveNotes,name='saveNotes'),
    #path('whats/',views.whats),
    #path('lognote/',views.lognote),
    #path('todo/check',views.check,name='check')
]
