from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum
import random
from .whats import *
from itertools import groupby
from operator import attrgetter 
from datetime import datetime 
from .PERSONS import Person
from django.contrib import auth
 
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
 



def jst(request):
    return render(request, 'jstest.html' )

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/Gotalking')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/Gotalking')
    else:
        return render(request, 'login.html', locals())

def notes(request):
    datas = getAllnotes()
    return render(request, 'notes.html',{'datas':datas})
def curseBook(request):
    return render(request, 'curseBook.html')
def main(request):
    return render(request,'main.html')
def getTodos(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        data = bulletNotemodel.objects.filter(content = title)
        note = {'title':data[0].content,'txt':data[0].txt}
        return JsonResponse({'response': title,'datas':note })
    return JsonResponse({'response': '...','datas':'...'})
 
def getNotes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        data = bulletNotemodel.objects.filter(Q(content=title)&Q(title='Note'))
        note = {'title':data[0].content,'txt':data[0].txt,'date':data[0].date}
        return JsonResponse({'response': title,'datas':note })
    return JsonResponse({'response': '...','datas':'...'})


def saveNotes(request):
    if request.method == 'POST': 
        # 获取POST请求中的参数
        tit = request.POST.get('tit')
        txt = request.POST.get('txt')
        date = request.POST.get('date')
        datas = getSameDate()
        # 在这里处理参数
        if tit :
            date = datetime.strptime(date,"%Y-%m-%d").date()
            note = bulletNotemodel.objects.get(Q(content =
                                                 tit)&Q(title='Note')&Q(date=date))
            note.txt = txt 
            note.save()
            return JsonResponse({'message': '参数已收到','datas':datas})
        else:
            return JsonResponse({'message': '缺少参数','datas':datas}, status=400)
    else:
        return JsonResponse({'message': '只接受POST请求','datas':datas}, status=405)
        
def saveTodos(request):
    if request.method == 'POST':
        datas = getSameDate()
        # 获取POST请求中的参数
        tit = request.POST.get('tit')
        done = request.POST.get('done')
        # 在这里处理参数
        if tit :
            todo = bulletNotemodel.objects.get(content = tit)
            todo.title = done 
            todo.save()
            return JsonResponse({'message': '参数已收到','datas':datas})
        else:
            return JsonResponse({'message': '缺少参数','datas':datas}, status=400)
    else:
        return JsonResponse({'message': '只接受POST请求','datas':datas}, status=405)

def addTH(request):
    return render(request, 'addTH.html' )


def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/main_page')

person = Person() 
def getSameDate():  #把資料輸出 [日期,A抬頭.A,B抬頭.B]
        
        items = []
        data = bulletNotemodel.objects.order_by('date')
        for key,group in groupby(data,key=attrgetter('date')):
            datal = []
            for g in group:
                st = '['+g.title+'] '+g.content
                datal.append(st)
            
            key = key.strftime("%Y-%m-%d")
            datal.append(key)
            datal.reverse()

            items.append(datal)
   
         
        items.reverse() 
        context = {
                'items':items
            }
        return context
 
def load_chat_html( request):
    return render(request, 'chat.html',{'inits':person.showCharact()} )
 
WHATS = {'HI':HI ,'TD':TODOs,'dowhat':SHOWTODO ,'boring':BORING,'sf':selFs}
SAYS = {'?':['不懂？','什麼？','？？？']}






def t(request):
    return render(request, 'login.html',{'OPEs':['HI','發呆']})


def ajaxt(request):
    what = request.POST.get('talks')
     
    response_data = {'message': '這是從伺服器返回的資料'}
    return JsonResponse(response_data)

class CHAT:
    def __init__(self):
        self.topic = None 


    def todosubmit(self,request):
        agree = request.POST.get('agree')
       
        if agree == 'true':
                # 資料傳送成功
                print('資料傳送成功')
        else:
                # 資料傳送失敗
                print('資料傳送失敗')
        return render(request, 'chat.html',{'inits':person.showCharact()} )
    



    def chating(self,request):
        if request.method == 'POST':
            print(request.POST)
            user_input = request.POST.get('user_input', '')
            chat_what = []
        # 在這裡處理用戶輸入，例如將其傳遞給AI模型進行處理並獲取回覆
        
            datas = getSameDate()
            if datas is None :
                datas = {'items':[]}
            if self.topic != None :
                if self.topic.isOver():
                    
                    self.topic = None
                else :
                    
                    chat_what = self.topic.OP(user_input)
                 
                
          
            if self.topic is None:

                if user_input[0] == 'Q' or user_input[0] == 'q':
                    topic = ADDTODO()
                    chat_what = topic.OP(user_input[1:])
                
                    return JsonResponse({'response': chat_what,'datas':datas})
                elif user_input[0] == '.' :
                    topic = ADDLOG()
                    
                    chat_what = topic.OP(user_input[1:])

                elif user_input in WHATS :
                    WH = WHATS[user_input]
                    self.topic = WH()
                    chat_what = self.topic.OP(user_input)
                    
                else :
                    says = SAYS['?']
                    waaa = random.choice(says) 
                    chat_what.append(waaa)
 
                    return JsonResponse({'response': chat_what,'datas':datas})

            # 假設chat_what是由AI模型回傳的回覆
            return JsonResponse({'response': chat_what,'datas':datas})
    

 
