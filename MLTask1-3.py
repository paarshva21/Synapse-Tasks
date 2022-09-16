class Titandex:
    def __init__(self,n,h,s):
        self.name=n
        self.height=h
        self.strength=s
        self.win_streak=0
    def TitanvsScout(self):
        print("Input number of battles between",self.name,"and Scouts:")
        n=int(input())
        for i in range(n):
            print("Enter Name of Scout and its Strength respectively:")
            scname=input()
            scstrength=int(input())
            if scstrength>self.strength:
                print("Winner is:",scname)
                if self.win_streak!=0:
                   print("Winning streak of",self.name,"is reset to zero")
                   self.win_streak=0
                else:
                   print("Winning streak is:",self.win_streak)
            elif scstrength==self.strength:
                print("Its a draw")
                if self.win_streak!=0:
                   print("Winning streak of",self.name,"is reset to zero")
                   self.win_streak=0
                else:
                   print("Wining streak is:",self.win_streak)
            else:
                self.win_streak=self.win_streak+1
                print("Winner is:",self.name)
                print("Winning streak is:",self.win_streak)
    def TitanvsTitan(self):
        print("Input number of battles between",self.name,"and Titans:")
        n=int(input())
        for j in range(n):
            print("Enter name of Titan and its Strength respectively:")
            tname=input()
            tstrength=int(input())
            if tname.lower()==(self.name).lower():
                print("A Titan cannot fight itself")
            elif tstrength>self.strength:
                print("Winner:",tname)
                if self.win_streak!=0:
                   print("Winning streak of",self.name,"is reset to zero")
                else:
                   print("Winning streak is:",self.win_streak)
            elif tstrength==self.strength:
                print("Its a draw")
                if self.win_streak!=0:
                   print("Winning streak of",self.name,"is reset to zero")
                   self.win_streak=0
                else:
                   print("Winning streak is:",self.win_streak)
            else:
                self.win_streak=self.win_streak+1
                print("Winner is:",self.name)
                print("Winning streak is:",self.win_streak)
a=input("Enter name of Titan:\n")
b=input("Enter height of Titan:\n")
c=input("Enter strength of Titan:\n")
titan=Titandex(a,int(b),int(c))      
titan.TitanvsScout()
titan.TitanvsTitan()