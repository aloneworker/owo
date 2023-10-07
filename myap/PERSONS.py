import random

class Person:
    def __init__(self):
        CHARACT = ['巨乳','瘦','翹臀','密大腿','大眼睛','紅唇']
        get = random.randint(0,3)
        self.charact = []
        for _ in range(get):
            what = random.choice(CHARACT)
            if what not in self.charact :
                self.charact.append(what)

    def showCharact(self):
        formatted_list = []
        for item in self.charact:
            formatted_list.append(f'[{item}]')
        output = '秘書的樣貌 ：'
        output += ' '.join(formatted_list)
        return output