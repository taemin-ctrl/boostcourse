#1-1
def gugudan(number):
    i=1
    while number*i<=50:
        print(number,'*',i,'=',number*i)
        i+=2
number = int(input("몇 단? : "))
gugudan(number)

#1-2
def gugudan(number):
    for i in range(1,51,3):
        if number*i<=50:
            print(number,'*',i,'=',number*i)
number = int(input("몇 단? : "))
gugudan(number)

#2
import random as rd
games = int(input("몇 판을 진행하시겠습니까? : "))

def rsp_advanced(games):
    i=0
    w=0
    l=0
    while i<games:
        i+=1
        a=int(input('가위=0,바위=1,보=2 중에 선택해주세요.: '))
        while a!=0 and a!=1 and a!=2:
            a = int(input("다시 선택해주세요. : "))
        b=rd.randint(0,2)
        if a==0 and b==1:
            print('나: 가위 컴퓨터: 바위\n',i,'번 째판 졌다.')
            l+=1
        elif a==0 and b==2:
            print('나: 가위 컴퓨터: 보\n',i,'번 째판 이겼다.')
            w+=1
        elif a==1 and b==2:
            print('나: 바위 \n컴퓨터: 보\n',i,'번 째판 졌다.')
            l+=1
        elif a==1 and b==0:
            print('나: 바위 \n컴퓨터: 가위\n',i,'번 째판 이겼다.')
            w+=1
        elif a==2 and b==1:
            print('나: 보 \n컴퓨터: 바위\n',i,'번 째판 이겼다.')
            w+=1
        elif a==2 and b==0:
            print('나: 보 \n컴퓨터: 가위\n',i,'번 째판 졌다.')
            l+=1
        elif a==0 and b==0:
            print('나: 가위 컴퓨터: 가위',i,'번째 판 비겼다.')
        elif a==1 and b==1:
            print('나: 바위 \n컴퓨터: 바위\n',i,'번째 판 비졌다.')
        else:
            print('나: 보 \n컴퓨터: 보\n',i,'번째 판 비겼다.')
    print('나의 전적',games,'전',w,'승',l,'패',games-w-l,'무')
    print('컴퓨터의 전적',games,'전',l,'승',w,'패',games-w-l,'무')
rsp_advanced(games)

#3
def find_even_number(n, m):
    print('첫 번째 수 입력 :',n)
    print('두 번째 수 입력 :',m)
    for i in range(n,int((m+n)/2)):
        if i%2==0:
            print(i,'짝수')
    if (m+n)/2%2==0:
        print(round((m+n)/2),'중앙값')
    for i in range(int((m+n)/2)+1,m+1):
        if i%2==0:
            print(i,'짝수')
n = int(input("첫 번째 수 입력해주세요. : "))
m = int(input("두 번째 수 입력해주세요. : "))
find_even_number(n, m)

#4
def count_prime_number(n, m):
    count=0
    for i in range(n,m+1):
         if i!=1:
            if i==2 or i==3 or i==5 or i==7 or i%2 !=0 and i%3 !=0 and i%5 !=0 and i%7 !=0 and i%11!=0:
                count+=1
    return print(count)
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)
