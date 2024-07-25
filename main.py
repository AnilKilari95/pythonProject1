class main:
    bno=0
    bnm=" "
    def disp(self):
        self.bno=100
        self.bnm="python"
        print(self.bno)
        print(self.bnm)
class book:
    anm=" "
    def disp1(self):
        self.anm="a.singh"
        print(self.anm)
class dbook(main,book):
    price=0.0
    def disp2(self):
        self.price=500
        super().disp()
        super().disp1()
        print(self.price)
obj=dbook()
obj.disp2()

class main:
    rno=0
    nm=" "
    def disp(self):
        self.rno=1
        self.nm="kumar"
        print(self.rno)
        print(self.nm)
class main1:
    mks=0.0
    def disp1(self):
        self.mks=75.0
        print(self.mks)
class main2(main,main1):
    grade=""
    def disp2(self):
        self.grade="A"
        super().disp()
        super().disp1()
        print(self.grade)
obj=main2()
obj.disp2()


class main:
    bno=0
    bnm=" "
    def disp(self):
        self.bno=100
        self.bnm="c++"
        print(self.bno)
        print(self.bnm)
class dmain(main):
    anm=" "
    def disp1(self):
        super().disp()
        self.anm="a.singh"
        print(self.anm)
class dmain1(main):
    pr=0
    def disp2(self):
        super().disp()
        self.pr=600
        print(self.pr)
obj=dmain()
obj1=dmain1()
obj.disp1()
obj1.disp2()


obj1=dmain1()
obj2=dmain2()
obj.disp1()
obj1.disp2()

