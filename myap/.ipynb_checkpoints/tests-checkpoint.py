from django.test import TestCase
from .models import *
from itertools import groupby
from operator import attrgetter 
import datetime ,random
# Create your tests here.
class modelTest(TestCase):

    def creatData(self):
        A = bulletNotemodel(title='Q',content='aaaaa',date=datetime.date(2023,8,10))
        b = bulletNotemodel(title='Q',content='b',date=datetime.date(2023,8,10))
        c = bulletNotemodel(title='@',content='c',date=datetime.date(2023,8,1))
        d = bulletNotemodel(title='#',content='feffef',date=datetime.date(2023,7,30))
        A.save()
        b.save()
        c.save()
        d.save()



      
    def test_date(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        print(today)
    def  t_data(self):
        self.earn('')
        what = input()
        self.earn_1(what)
        self.earn('')
        what = input()
        self.earn_1(what)
        self.earn('')
        what = input()
        self.earn_1(what)
        self.earn('')
        what = input()
        self.earn_1(what)


    def earn(self,param):
         
        keyWord = ['巨乳']#,'翹臀','垂奶','挺奶','長腿','蜜唇','長髮','魅眼','水蛇腰','蜜桃臀','蜜大腿']
        descriptType = ['生氣','開心','一般','主動交配','被動交配','主動NTR','被動NTR','高潮']
        self.key = random.choice(keyWord)
        self.typ = random.choice(descriptType)
        print('你現在跟一個[{}]的妹子在一起，妹子的狀態[{}]請你描述妹子的反應'.format(self.key,self.typ))

    def earn_1(self,param):
        
        char ,created = charact.objects.get_or_create(keyWord=self.key)
      
 

 
        



'''         完成的寒士



    def showDo(self,param):
        if data:
            what = bulletNotemodel.objects.filter(title='Q')
            what = random.choice(what)
            return what.content
        else :
            return '沒有工作！'

    def getSameDate(self):#把資料輸出 [日期,A抬頭.A,B抬頭.B]
        self.creatData()
        items = []
        data = bulletNotemodel.objects.order_by('date')
        for key,group in groupby(data,key=self.outDate):
            datal = []
            for g in group:
                st = g.title+'.'+g.content
                datal.append(st)
             
        
            datal.append(key)
            datal.reverse()
            
            items.append(datal)
   
         
        
        context = {
                'items':items
            }
''' 


