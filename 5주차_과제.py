#1
import random as rd
bs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] 
while True:
    my=input('My turn - 숫자를 입력하세요: ').split()   
    count=0
    while True:
        for i in range(0,len(my)):
            if my[i]!=str(bs[i]):
                count=1
        if count==0 and len(my)<=3:
            break   
        my=input('My turn - 숫자를  다시 입력하세요: ').split()
        count=0
    for j in my:
        bs.remove(int(j))
    if len(bs)==1:
        print('이겼습니다.')
        break
    try:
        for _ in range(rd.randint(1,3)):
            bs.remove(bs[0])
        print('현재 숫자:',my[-1])
        for k in range(int(my[-1])+1,bs[0]):
            print('컴퓨터:',k)
        print('현재 숫자:',bs[0]-1)
    except:
        print('졌습니다.')
        break

#2
def grader(s, a):
    count=0
    lis=[]
    re_lis=[]
    for j in range(0,len(s)):
        for i in range(0,10):
            if (s[j])[i+3]==str(a[i]):
                count+=1
        lis.append(count)
        re_lis.append(count)
        count=0
    re_lis.sort(reverse=True)
    for k in range(0,len(s)):
        print(f'학생: {(s[lis.index(re_lis[k])])[:2]} 점수: {re_lis[k]*10}점 {k+1}등')
s = ["김갑,3242524215","이을,3242524223","박병,2242554131","최정,4245242315","정무,3242524315"]
a = [3,2,4,2,5,2,4,3,1,2]
grader(s,a)

#3
import random as rd
import statistics as s
num1=rd.randint(0,100)
num2=rd.randint(0,100)
num3=rd.randint(0,100)
lis=[num1,num2,num3]
#lis=[2,50,100]
m=s.median(lis)
l=max(lis)
s=min(lis)
you=[]
count=1
a=int(input(f'{count}차시도\n숫자를 예측해보세요 :'))
while True:
    count+=1   
    if a in you:
        print('이미 예측에 사용한 숫자입니다')
    else:
        if a in lis:
            lis.remove(a)
            if a is l:
                print(f'정답입니다.{a}는 최댓값입니다.')
            elif a is s:
                print(f'정답입니다.{a}는 최솟값입니다.')
            else:
                print(f'정답입니다.{a}는 중간값입니다.')        
        else:
            print(a,'는 없습니다')
    you.append(a)            
    if len(lis)==0:
        break
    if count>5:
        if a>l:
            print('최댓값은',a,'보다 작습니다.')
        elif a<s:
            print('최솟값은',a,'값보다 큽니다.')
        else:
            print(a,'는 최댓값과 최솟값 사이에 있습니다.')    
    a=int(input(f'{count}차시도\n숫자를 예측해보세요 :'))
print('게임종료')
print(count,'번 시도만에 예측 성공')

#4
def after_100(a,b,c):
    d=['월','화','수','목','금','토','일']
    e=[31,28,31,30,31,30,31,31,30,31,30,31]
    mon=a+3
    day= e[a-1]-b
    count=0
    for i in range(0,10):
        day+=e[a+i]
        count+=1
        if day>100:
            break
    day=99-(day-e[a+count-1])
    if count==4:
        mon+=1
    days=d[d.index(c)+1]
    return print(f'{mon}월 {day}일 {days}요일')
after_100(3,31,'화')
