import openai
import os 
import time
from django.conf import settings
 
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
        self.cursePower = 0
        self.getcursePower()
        self.status = 'home'
        self.cards = [] 
        self.newcards = 0
        self.meet_times = 0

    
    def t(self,request):
        return render(request,'TEST_WORD/TEST.html')
    def start(self,request):
        if request.user.is_authenticated:
            self.getcurse()
            return render(request, 'main.html',{'curses':self.curses})
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

    def startDrink(self,request):
        request.session['start_time'] = time.time()

    def meetlv(self,request):
        start_time = request.session.get('start_time')
        if start_time:
            elapsed_time = time.time() - start_time
            minutes_passed = int(elapsed_time / 60)
            if minutes_passed > 30:
                minutes_passed = 30  # 限制最大30分钟

            # 计算获取S卡的概率
            chance = 1 + (minutes_passed * 0.1333)  # 基本概率1%，每分钟增加0.1333%
            chance = min(chance, 5)  # 限制最大概率为5%
            
            # 决定是否给予S卡
            if random.random() * 100 < chance:
                card = 'S'
            else:
                card = 'n'
            return card
    def Drinktimeout(self,request):
        start_time = request.session.get('start_time')
        if start_time:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 1800:  # 30分鐘為1800秒
                return True
            else :
                return False 
        
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

    def spendCursePower(self,point):
        if self.cursePower >= point :
            self.cursePower -= point 
            return True
        return False 
    
    def talking(self,request):
        if request.method == 'POST':
            user_input = request.POST.get('talks')
             
            if user_input == '酒吧':
                self.status = 'bar'
                self.getcursePower()
                
                return JsonResponse({'response':'喝酒嗎 ? 10 咒喝一杯 y '.format(self.cursePower),'images':''})

            if user_input == 'y' and self.status == 'bar':
                if self.spendCursePower(10) :
                    self.status = 'bar_serchGirl'
                    self.meet_times = 0 
                    self.startDrink(request)
                    return JsonResponse({'response':'喝著酒..看看有沒有妹子! '.format(self.cursePower),'images':''})               
                return JsonResponse({'response':'你的咒不夠!! '.format(self.cursePower),'images':''})  

            if self.status == 'bar_serchGirl':
                if self.Drinktimeout(request):
                    self.status = 'bar'
                    return JsonResponse({'response':'時間到了!! '.format(self.cursePower),'images':''})  
                self.meet_times += 1 
                chance = self.meet_times + 7
                if random.randint(0,chance) <3:
                    lv = self.meetlv(request)
                    return JsonResponse({'response':'你遇到了一個妹子!!{} '.format(lv),'images':''}) 
                else :
                    return JsonResponse({'response':'沒 ','images':''}) 
                
            
            if self.status == 'store' and user_input == 'y' :
                if self.spendCursePower(10) :
                    self.status = 'draw'
                    self.newcards = 5
                    return JsonResponse({'response':'你買了一包卡包!!' ,'images':''})
                else :
                    self.status = 'home'
                    return JsonResponse({'response':'你的咒不夠!! 滾啦!... '.format(self.cursePower),'images':''})

            if self.status == 'draw' and self.newcards > 0 :
                card = random.randint(1,3)
                self.cards.append(card)
                self.newcards -= 1 
                if self.newcards == 0 :
                    return JsonResponse({'response':'抽開!!! 你抽到 {}!!  沒有了~!'.format(card).format(self.cursePower),'images':''})
                return JsonResponse({'response':'抽開!!! 你抽到 {}!!'.format(card).format(self.cursePower),'images':''})
                
                
            if user_input == 'newNote':
                title = request.POST.get('title')
                notes = request.POST.get('note')
                today = datetime.datetime.now()
                today = today.strftime('%Y-%m-%d')
                note = bulletNotemodel(title='Note',date=today,content=title,txt=notes)
                note.save()
                self.reflashBook()
                return JsonResponse({'response':'加入!','images':''})
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
                    today = datetime.datetime.now()
                    note.date = today
                    note.save()
                self.reflashBook()
                return JsonResponse({'response':'加入!','images':''})
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
                                             chat_what,'datas':self.notes,'images':''})
                    if user_input[0] == '@' :
                        obj = user_input[1:]
                        if obj == '' :
                            topic = whatNotes()
                            self.notes = topic.OP('@')
                            return JsonResponse({'response': chat_what,'datas':datas,'images':''}) 
                        today = datetime.datetime.now()
                        today = today.strftime('%Y-%m-%d')
                        tod = bulletNotemodel(title='@',date=today,content=obj)
                        tod.save()
                        self.reflashBook()
                        return  JsonResponse({'response': chat_what,'datas':datas,'images':''})
                    elif user_input[0] == '^':
                        obj = user_input[1:]
                        if len(self.curses)>=3+self.curseLv :
                            return JsonResponse({'response':'咒書已滿!','images':''})
                        else :
                            #self.curses.append(obj)
                            item = bulletNotemodel.objects.get(id=id_)
                            item.title = "咒"
                            item.save()
                            self.notes = getAllnotes()
                            return JsonResponse({'response':'加入!','images':''})
                    elif user_input[0] == '☞':
                        obj = user_input[1:]
                        item = bulletNotemodel.objects.get(id=id_)
                        item.delete()
                        self.notes = getAllnotes()
                        return JsonResponse({'response':'刪除了!','images':''})
                    elif user_input[0] == '~':
                        obj = user_input[1:]
                        item = bulletNotemodel.objects.get(id=id_)
                        item.title = '[誌]'
                        item.save()
                        self.notes = getAllnotes()
                        return JsonResponse({'response':'改了','images':''})
                    elif user_input[0] == '$':
                        obj = user_input[1:]
                        item = bulletNotemodel.objects.get(id=id_)
                        item.title = '@'
                        item.save()
                        self.notes = getAllnotes()
                        return JsonResponse({'response':'改了','images':''})

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
                        self.curses = self.curses.exclude(id = id_)
                        point = random.randint(10,30)
                        self.cursePower -= point
                        self.cursePowerchange(0)
                        self.notes = getAllnotes()
                        return JsonResponse({'response':'咒退回!使用 '+str(point)+'咒力','images':''})

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
                        return JsonResponse({'response':'消除成功!獲 '+str(point)+'咒力','images':''})
                    if user_input[0] == '?' :
                        topic = whatNotes()
                        obj = user_input[1:]
                        if obj == '' :
                            chat_what = "NO???"
                        else :
                            self.notes = topic.OP(obj)
                            chat_what = "我馬上查詢" ;
                        return  JsonResponse({'response':
                                              chat_what,'datas':self.notes,'images':''})
                    if user_input[0] == '#' :
                        obj = user_input[1:]
                        if obj == '' :
                            return  JsonResponse({'response': chat_what,'datas':datas,'images':''})

                        topic = ADDEVENT()
                        topic.OP(obj)
                        self.reflashBook()
                        return  JsonResponse({'response': chat_what,'datas':datas,'images':''})


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
     
                        return JsonResponse({'response': chat_what,'datas':datas,'images':''})
            # 假設chat_what是由AI模型回傳的回覆
            self.reflashBook()
            return JsonResponse({'response': chat_what,'datas':datas,'images':''})
    


    def play(self,request):
        if request.user.is_authenticated:
            return render (request,'playin.html',{'datas':self.notes})
        return HttpResponseRedirect('/')







