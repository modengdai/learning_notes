import random
def main():
    PrintInfo()
    a,b,n=GetData()
    ProbA,ProbB=SimNGames(a,b,n)
    PrintResult(ProbA,ProbB)
def PrintInfo():
    print("这是一场模拟n次必比赛的小程序\n通过给定两人的赢球概率，比赛场次，得出获胜概率\
          游戏规则为：只能发球方得分，发球方得分后继续发球\
          发球方未得分，改由对方发球")
          
def GetData():
    a=eval(input("请输入甲方赢球概率"))
    b=eval(input("请输入乙方赢球概率"))
    n=eval(input("请输入比赛模拟次数"))
    return a,b,n

def SimNGames(a,b,n):           #x循环n次
    CountA=CountB=0      
    for i in range(n):
        ScoreA,ScoreB=SimOneGame(a,b)
        if ScoreA>ScoreB:
            CountA +=1
        else:
            CountB +=1

    ProbA=CountA/n
    ProbB=CountB/n
    return ProbA,ProbB

def SimOneGame(a,b):
   
    x=random.choice('ab') 
    ScoreA=ScoreB=0
    while not GameOver(ScoreA,ScoreB):
        if x=='a':
            if random.random()<=a:
              ScoreA+=1
              x='a'
            else:
              x='b'
        if x=='b':
            if random.random()<=b:
              ScoreB+=1
              x='b'
            else:
              x='a'  
    return ScoreA,ScoreB

def GameOver(ScoreA,ScoreB): 
    return   ScoreA==15 or ScoreB==15

def PrintResult(ProbA,ProbB):
          print("A胜出的概率为",ProbA)
          print("B胜出的概率为",ProbB)
          
main()          
          
          
          
