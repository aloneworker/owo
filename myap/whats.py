from .models import *
from django.db.models import Q
import random
import datetime
from itertools import groupby
from operator import attrgetter 
import datetime 
from django.contrib import auth



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

def savenotes(title,notes):
    today = datetime.datetime.now()
    today = today.strftime('%Y-%m-%d')
    tod = bulletNotemodel(title='Note',date=today,content=title,txt=notes)
    tod.save()



class BASE:

    def __init__(self):
        self.step = 0
        self.STEPOP = []
        self.over = False 
        self.setSTEPOP()
        
 
    def setSTEPOP(self):
        pass
 
    def OP(self,param=None):
        if self.step < len(self.STEPOP):
            OP = self.STEPOP[self.step]
 
            self.step += 1
            return OP(param)
        
        self.over = True
        return ['.....']

    def isOver(self):
        return self.over

class selFs(BASE):
    def __init__(self):
        super().__init__()
        self.showL = False
        self.talks = []
    def setSTEPOP(self):
        self.STEPOP = [self.star,self.repet]

    def star(self,param):
        return ['開始～～']

    def repet(self,param):
 
        self.STEPOP.append(self.repet)
        if param == 'ed' :
            self.over = True
        elif param == 'showl':
            return self.talks
        else :
            self.talks.append(param)
            return [param+' ??'] 

class HI(BASE):
    def OUT(self,param=None):
       self.over = True
       return ['HI'] 
    def setSTEPOP(self):
        self.STEPOP = [self.OUT]

class NOTEING(BASE):
    def __init__(self):
        super().__init__()

    def setSTEPOP(self):
        self.STEPOP = [self.showNOTE]

    def showNOTE(self,param):
        self.over = True
        return ['showNOTE|0']
    


class EARN(BASE):
    def __init__(self):
        super().__init__()

    def setSTEPOP(self):
        self.STEPOP = [self.addcharact]

    def addcharact(self,param):
 
        pass
        return [param+'加入！！']
    


class ADDNote(BASE):
    def __init__(self):
        super().__init__()

    def setSTEPOP(self):
        self.STEPOP = [self.adding]

    def adding(self,param):
        tod = bulletNotemodel(title='@',content=param,)
        tod.save()
        return [param+'加入！！']

class SHOWTODO(BASE):
    def __init__(self):
        super().__init__()
                
 
    def setSTEPOP(self):
        self.STEPOP = [self.Q,self.showDo]

    def Q(self,param):
        return ['今天要做什麼呢？(1:很重要的,2:有點急,3:,4:,5:)?']
    
    def showDo(self,param):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        items = bulletNotemodel.objects.filter(title='Q',order=param)
        items = items.exclude(checkDa=today)
        item = []
        for it in items:
            item.append(it.name)

        if len(item) < 1 :
            return ['沒有工作喔！！']

        return item
    
class BORING(BASE):
    def __init__(self):
        super().__init__()
        data = bulletNotemodel.objects.filter(Q(title='Q')&Q(order='1'))
        if data:
            self.what = random.choice(data)
        else :
            self.what = None

    def setSTEPOP(self):
        self.STEPOP = [self.showDo,self.checkDone]

    def checkDone(self,param):
        talks = ['幹的好阿！','好拉 給你看一下奶子！ (露出巨乳)']
        talkchar = [
    "一個女秘書，身材姣好，巨乳蜜桃臀，穿著暴露。",
    "女秘書生氣了，眉頭緊鎖，臉上帶著不耐煩的表情。",
    "走路時，乳房微微下垂，隨著動作搖動，吸引眾人目光。",
    "她的臀部在每一步都輕輕擺動，散發出優雅的魅力。",
    "當她生氣時，乳房似乎更加顯眼，微微的搖晃傳遞著不滿情緒。",
    "女秘書站在辦公桌前，手指敲擊著桌面，眼神中帶著一絲怒意。",
    "她的乳房在呼吸間輕輕起伏，給人一種性感的視覺感受。",
    "身穿暴露服裝的她，緊繃的臀部緩緩擺動，引人入勝。",
    "女秘書擡頭看著文件，乳房微微搖晃，似乎在尋找靈感。",
    "她的表情變幻莫測，不耐煩的情緒通過眼神傳遞出來。",
    "在她走來走去的過程中，乳房的輕微擺動成為焦點。",
    "女秘書的臀部緩緩擺動，散發著迷人的曲線美。",
    "穿著暴露的服裝更凸顯了她的優美身姿，乳房輕輕搖曳。",
    "她的動作流暢而優雅，乳房的輕微擺動仿佛有著自己的節奏。",
    "女秘書的表情中帶著一絲不滿，乳房隨著她的情緒起伏。",
    "走路時，她的臀部輕輕擺動，線條優美而引人注目。",
    "女秘書的乳房微微下垂，隨著她的動作輕輕擺動。",
    "她的表情充滿不耐煩，乳房輕輕晃動，顯得更加迷人。",
    "女秘書的臀部在走路時輕輕擺動，散發著一種優雅的魅力。",
    "她生氣地咬著下唇，乳房微微顫抖，帶著挑釁的姿態。"
]

        talkAng = ['不要開玩笑好嗎？['+self.what.content+']！！！','快把['+self.what.content+']工作完成！！！']
        if param == 'DONE' :
            self.over = True
            self.what.done = True
            self.what.title = '完成'
            self.what.save()
            self.what = None
            return [random.choice(talks)]
        elif param == 'PASS':
            self.over = True 
            talk = [random.choice(talkchar),'先這樣吧...']
            return talk
        else :
            self.STEPOP.append(self.checkDone)
            talk = [random.choice(talkchar)]
            talk.append(random.choice(talkAng))
            return  talk
    def showDo(self,param):
        if self.what is None:
            self.over = True
            return ['沒有工作喔！！']
        
        talks = [    "女秘書，身材傲人，擁有巨乳和蜜桃臀，總是穿著暴露的服裝，讓人忍不住注目。", 
                     "她走路時，臀部優雅地擺動，每一步都彷彿在引領節奏。",
                     "乳房微微的下垂，但隨著她的動作，它們輕輕搖擺，仿佛是音樂中的節拍。",
                     "每次她走進辦公室，同事們的目光都會不自覺地被她的魅力所吸引。",    "她的臉上總是帶著自信的微笑，展現出她對工作的熱情。",    "有一天，她在會議中主動提出：「我可以幫你做這個任務嗎？」",    "她的聲音柔和而自信，讓人難以拒絕。",    "在完成工作的過程中，她總是充滿活力，讓整個辦公室都感受到了她的積極態度。",    "就像她的乳房和臀部一樣，她的工作態度也是充滿動感和活力的。",    "同事們都很樂意與她合作，因為她不僅專業，而且樂於助人。",    "這次的dotolist工作，她輕鬆地接受了：「當然可以幫你做這個，我會盡快完成的。」"]

        talking = [random.choice(talks)]        
       
        what = '請把 ['+self.what.content+'] 完成好嗎？ (完成請打 DONE)'
        talking.append(what)
        return talking
 
class doSomething(BASE):
    def __init__(self):
        super().__init__()
        data = bulletNotemodel.objects.filter(Q(title='Q')&Q(order='1'))
        if data:
            self.what = random.choice(data)
        else :
            self.what = None


    def setSTEPOP(self):
        self.STEPOP = [self.shows]


    def shows(self,param):
        if self.what is None:
            self.over = True
            return ['沒有工作喔！！']
 
        what = '請完成 [ '+self.what.content+' ] ' 
        
        
        return ['|'+what]    

class ADDTHI(BASE):
    def __init__(self):
        super().__init__()


    def setSTEPOP(self):
        self.STEPOP = [self.adding]


    def adding(self,param):
        today = datetime.datetime.now()
        today = today.strftime('%Y-%m-%d')
        tod = bulletNotemodel(title='思',date=today,content=param,)
        tod.save()
        return [param+'加入！！']


class ADDTODO(BASE):
    def __init__(self):
        super().__init__()


    def setSTEPOP(self):
        self.STEPOP = [self.adding]


    def adding(self,param):
        today = datetime.datetime.now()
        today = today.strftime('%Y-%m-%d')
        tod = bulletNotemodel(title='Q',date=today,content=param,)
        tod.save()
        return [param+'加入代辦事項了！！']

class ADDLOG(BASE):
    def __init__(self):
        super().__init__()


    def setSTEPOP(self):
        self.STEPOP = [self.adding]


    def adding(self,param):
        talks = [
 "身穿著暴露的女秘書，她的體態正散發著自信，巨乳引人注目，仿佛是自然的奇蹟。",
 "在這個情境下，女秘書的乳房下垂且圓潤，散發出一種優雅的美感，宛如藝術品。",
 "她的巨乳在薄紗下微微顫動，如同一對誘人的雕塑，令人難以移開目光。",
 "乳房的形狀如同柔軟的半球，溫柔地彎曲，細膩的肌膚上繪著淡淡的曲線。",
 "每一個細節都被描繪得栩栩如生，從乳暈的輕微隆起到乳房的柔軟觸感。",
 "雖然乳房下垂，但這種自然的變化為她增添了成熟的魅力，讓人不由得想要探索更多。",
 "她的巨乳似乎是生活的見證，每一個紋理都蘊含著豐富的故事。",
 "微微上揚的乳暈被微風輕拂，彷彿在訴說著一個屬於她自己的秘密。",
 "乳房的肌膚散發出淡淡的香氣，讓人陶醉其中，彷彿置身於花園之中。",
 "正露出的巨乳在陽光下閃耀著微光，如同一個魅惑的寶盒，充滿神秘感。",
 "與她的體態相得益彰的巨乳，仿佛是完美比例的象徵，讓人難以抗拒。",
 "乳房的形狀猶如月亮的弧度，圓潤而溫柔，令人感受到無限的撫慰。",
 "裹挾著微妙的重量，乳房的輕微下垂反而賦予了她一種優雅的氣質。",
 "她站在那裡，乳房如詩如畫，讓人產生無限的遐想和美好的聯想。",
 "巨乳在穿著暴露的情境下，彷彿是對自然美的讚歌，為整個場景增色不少。",
 "乳房的樣貌宛如雕刻，每一處紋理都透露出她的個性和獨特之處。",
 "她的乳房仿佛是一幅藝術品，每一筆每一線都是大師級的巧思和創意。",
 "乳房的柔軟觸感讓人難以忘懷，彷彿能夠感受到其中蘊含的情感。",
 "在這個情境下，女秘書的巨乳彷彿是一道風景，吸引著眾人的目光。",
 "她的乳房是完美的曲線，如同大自然賦予的禮物，散發出一種不可抵擋的魅力。"
]
        today = datetime.datetime.now()
        today = today.strftime('%Y-%m-%d')
        

        tod = bulletNotemodel(title='[誌]',content=param,date=today)
        tod.save()
        talking = [random.choice(talks)]
        talking.append('好的！我幫你加入手帳')
        return [talking]
    

class TODOs(BASE):
    def __init__(self):

        today = datetime.datetime.now().strftime("%Y-%m-%d")

        self.items = bulletNotemodel.objects.filter(title='Q')
        self.items  = self.items.exclude(checkDa=today)
        super().__init__()
 
    def setSTEPOP(self):
        if len(self.items) < 1 :
            self.STEPOP = [self.NOTODO]
        else :
            self.STEPOP = [self.star,self.oneyesOP]
            for _ in range(len(self.items)) :
                self.STEPOP.append(self.yesOP)
          

    def NOTODO(self,param):
        self.over = True 
        return ['NO work!!'] 

    def star(self,param):
        return ['開始今天的工作＠＠ y? ']
    
    def oneyesOP(self,param):
     
        if param == 'y' or param == 'yes' :
            item = self.items[self.step-2]
            return ['['+item.content+'] 的優先順序是？[1~5] or done[d]']
        else :
            self.over = True
            return ['好吧！下次見 ！！']

    def yesOP(self,param):
        talks = []
        print(self.step)
        today = datetime.datetime.now().strftime("%Y-%m-%d")
 
        if param.isdigit():
            item = self.items[self.step-3] 
            talks.append('['+item.content+'] 優先順序是' + param) 
            item.order = param
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            item.checkDa = today
            item.save()
        elif param == 'd':
            item = self.items[self.step-3] 
            talks.append('['+item.content+'] 完成！恭喜～～' ) 
            item.order = param
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            item.checkDa = today
            item.title = '完成'
            item.save()  
        if self.step <= len(self.items):
            item = self.items[self.step-2]
            talks.append('['+item.content+'] 的優先順序是？[1~5]')
        else :
            self.over = True
            talks.append(['設定完成！！可喜可賀'])
        
        return talks
 
 
        


    def isOver(self):
        return self.over 
