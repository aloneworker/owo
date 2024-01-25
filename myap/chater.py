import openai
import os  
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum
import random
from .whats import *
from itertools import groupby
from operator import attrgetter 
import datetime 
from .PERSONS import Person
from django.http import  HttpResponseRedirect
from django.contrib import auth

WHATS = {'HI':HI ,'TD':TODOs,'dowhat':SHOWTODO
         ,'boring':BORING,'sf':selFs,'發呆':seeWhat,
         'note':NOTEING,'test':seeWhat,'zzz':seeWhat}
SAYS = {'?':['不懂？','什麼？','？？？']}


person = Person() 


class oWo_:
    def __init__(self):
        self.topic = None
        self.notes = None
        self.notes = getAllnotes()
        self.curses = []
        self.curseLv = 0
        self.getcurse()
        self.getcursePower()
    def start(self,request):
        if request.user.is_authenticated:
            return render(request, 'main.html')
        return HttpResponseRedirect('/')
    def getcurse(self):
        self.curses = bulletNotemodel.objects.filter(title = '咒')
        #for curse in curses :
         #   self.curses.append(curse.content)
    def cursePowerchange(self,param):
        point = int(param)
        self.cursePower += point
        self.saveCurse()


    def reflashBook(self):
        self.notes = getAllnotes()


    def saveCurse(self):

        condition_A = {'title': '[誌]'}  # 替換為您的條件A
        condition_B = {'content': '咒力'}  # 替換為您的條件B

        # 使用filter()方法來查找具有條件A和條件B的資料記錄
        matching_records = bulletNotemodel.objects.filter(**condition_A,**condition_B).first()

        matching_records.txt = self.cursePower
        matching_records.order = self.curseLv
        matching_records.save()

    def getcursePower(self):
        condition_A = {'title': '[誌]'}  # 替換為您的條件A
        condition_B = {'content': '咒力'}  # 替換為您的條件B

        # 使用filter()方法來查找具有條件A和條件B的資料記錄
        matching_records = bulletNotemodel.objects.filter(**condition_A , **condition_B)

        if matching_records.exists():
        # 找到符合條件的資料記錄，取第一個（或根據需求進一步選擇）
            existing_record = matching_records.first()
            self.cursePower = int(existing_record.txt)
            self.curseLv = int(existing_record.order)

        else:
        # 找不到符合條件的資料記錄，創建一個新的資料記錄
            new_record = bulletNotemodel(**condition_A, **condition_B)
            new_record.txt = 0
            today = datetime.datetime.now()
            today = today.strftime('%Y-%m-%d')
            new_record.date = today
            new_record.save()
            self.curseLv =0
            self.cursePower = 0
    def noteWeb(self,request):
        if request.user.is_authenticated:
            return render (request,'notes.html',{'datas':self.notes})
        return HttpResponseRedirect('/')
    def curseBook(self,request):
        if request.user.is_authenticated:
            self.getcurse()
            return render(request,'curseBook.html',{'curses':self.curses})
        return HttpResponseRedirect('/')
    def noteSAVE(self,request):
        if request.method == 'POST':
            data = request.POST.get('data')
            datas = data.split('|')
            savenotes(datas[0],datas[1])
        return JsonResponse({'response': 'ok'})

    def talking(self,request):
        if request.method == 'POST':
            user_input = request.POST.get('talks')
            if user_input == 'newNote':
                title = request.POST.get('title')
                notes = request.POST.get('note')
                today = datetime.datetime.now()
                today = today.strftime('%Y-%m-%d')
                note = bulletNotemodel(title='Note',date=today,content=title,txt=notes)
                note.save()
                self.reflashBook()
                return JsonResponse({'response':'加入!'})
            elif user_input == "edNote":
                title = request.POST.get('tit')
                id_ = request.POST.get('id')
                if title == '':
                    note = bulletNotemodel.objects.get(id = id_)
                    note.delete()
                else :
                    note = bulletNotemodel.objects.get(id=id_)
                    note.content = title
                    txt = request.POST.get('txt')
                    note.txt = txt
                    note.save()
                self.reflashBook()
                return JsonResponse({'response':'加入!'})
            elif user_input == "NOTE":
                use = whatNotes()
                self.notes = use.OP('Note')
            elif user_input == "ALL":
                use = whatNotes()
                self.reflashBook()
            elif user_input == "LOG":
                use = whatNotes()
                self.notes = use.OP("[誌]")
                
            id_ = request.POST.get('id')
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
                if user_input != '' :
                    if user_input[0] == 'Q' or user_input[0] == 'q':
                        if user_input[1:] == '':
                            topic = whatNotes()
                            self.notes = topic.OP('Q')
                            return JsonResponse({'response': chat_what,'datas':datas}) 
                        topic = ADDTODO()
                        chat_what = topic.OP(user_input[1:])
                        self.reflashBook()
                        return JsonResponse({'response':
                                             chat_what,'datas':self.notes})
                    if user_input[0] == '@' :
                        obj = user_input[1:]
                        if obj == '' :
                            topic = whatNotes()
                            self.notes = topic.OP('@')
                            return JsonResponse({'response': chat_what,'datas':datas}) 
                        today = datetime.datetime.now()
                        today = today.strftime('%Y-%m-%d')
                        tod = bulletNotemodel(title='@',date=today,content=obj)
                        tod.save()
                        self.reflashBook()
                        return  JsonResponse({'response': chat_what,'datas':datas})
                    elif user_input[0] == '^':
                        obj = user_input[1:]
                        if len(self.curses)>=3+self.curseLv :
                            return JsonResponse({'response':'咒書已滿!'})
                        else :
                            #self.curses.append(obj)
                            item = bulletNotemodel.objects.get(id=id_)
                            item.title = "咒"
                            item.save()
                            self.notes = getAllnotes()
                            return JsonResponse({'response':'加入!'})
                    elif user_input[0] == '☞':
                        obj = user_input[1:]
                        item = bulletNotemodel.objects.get(id=id_)
                        item.delete()
                        self.notes = getAllnotes()
                        return JsonResponse({'response':'刪除了!'})

                    elif user_input[0] == '☄':
                        obj = user_input[1:]
                        log =bulletNotemodel.objects.get(id=id_)
                        log.title = '@'
                        log.save()
                        self.notes = getAllnotes()

                    elif user_input[0] == '}':
                        obj = user_input[1:]
                        id_ = request.POST.get('id')
                        curse =bulletNotemodel.objects.get(id=id_)
                        curse.title = 'Q'
                        curse.save()
                        self.curses - self.curses.exclude(id = id_)
                        point = random.randint(10,30)
                        self.cursePower -= point
                        self.cursePowerchange(0)
                        self.notes = getAllnotes()
                        return JsonResponse({'response':'咒退回!使用 '+str(point)+'咒力'})

                    elif user_input[0] == '✔':
                        obj = user_input[1:]
                        id_ = request.POST.get('id')
                        curse =bulletNotemodel.objects.get(id=id_)
                        curse.title ='完成'
                        today = datetime.datetime.now()
                        today = today.strftime('%Y-%m-%d')
                        curse.date = today
                        curse.save()
                        self.curses = self.curses.exclude(id = id_)
                        point = random.randint(4,12)
                        self.cursePowerchange(point)
                        self.notes = getAllnotes()
                        return JsonResponse({'response':'消除成功!獲 '+str(point)+'咒力'})
                    if user_input[0] == '?' :
                        topic = whatNotes()
                        obj = user_input[1:]
                        if obj == '' :
                            chat_what = "NO???"
                        else :
                            self.notes = topic.OP(obj)
                            chat_what = "我馬上查詢" ;
                        return  JsonResponse({'response':
                                              chat_what,'datas':self.notes})
                    if user_input[0] == '#' :
                        obj = user_input[1:]
                        if obj == '' :
                            return  JsonResponse({'response': chat_what,'datas':datas})

                        topic = ADDEVENT()
                        topic.OP(obj)
                        self.reflashBook()
                        return  JsonResponse({'response': chat_what,'datas':datas})


                    if user_input == 'logout':
                        auth.logout(request)
                        chat_what = ['登出！！']

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
            self.reflashBook()
            return JsonResponse({'response': chat_what,'datas':datas})
    


    def play(self,request):
        if request.user.is_authenticated:
            return render (request,'playin.html',{'datas':self.notes})
        return HttpResponseRedirect('/')







