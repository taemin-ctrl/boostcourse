# 1
import random as rd
a=input('가위,바위,보 중에 선택해주세요.: ')
while a!='가위' and a!='바위' and a!='보':
    a=input('다시 정확히 적어주세요.: ')
numlist=['가위','바위','보']
b=rd.choice(numlist)
print('나: ',a,'\n컴퓨터: ',b)

if a=='가위' and b=='바위':
    print('졌다.')
elif a=='가위' and b=='보':
    print('이겼다.')
elif a=='바위' and b=='보':
    print('졌다.')
elif a=='바위' and b=='가위':
    print('이겼다.')
elif a=='보' and b=='바위':
    print('이겼다.')
elif a=='보' and b=='가위':
    print('졌다.')
else:
    print('비겼다.')

# 1.1 추가
import random as rd
a=int(input('가위=0,바위=1,보=2 중에 선택해주세요.: '))
b=rd.randint(0,2)
if a==0 and b==1:
    print('나: 가위 \n컴퓨터: 바위\n졌다.')
elif a==0 and b==2:
    print('나: 가위 \n컴퓨터: 보\n이겼다.')
elif a==1 and b==2:
    print('나: 바위 \n컴퓨터: 보\n졌다.')
elif a==1 and b==0:
    print('나: 바위 \n컴퓨터: 가위\n이겼다.')
elif a==2 and b==1:
    print('나: 보 \n컴퓨터: 바위\n이겼다.')
elif a==2 and b==0:
    print('나: 보 \n컴퓨터: 가위\n졌다.')
elif a==0 and b==0:
    print('나: 가위 \n컴퓨터: 가위\n비겼다.')
elif a==1 and b==1:
    print('나: 바위 \n컴퓨터: 바위\n비졌다.')
else:
    print('비겼다.')

# 2.
def money(mon,tax):
    k=12*mon*(100-tax)/100
    return round(k)
c=int(input('월급을 입력해주세요.(단위:만원): '))
a=c*12
b=0
if a<=1200:
    b=6
elif a<=4600:
    b=15
elif a<=8800:
    b=24
elif a<=15000:
    b=35
elif a<=30000:
    b=38
elif a<=50000:
    b=40
else:
    b=42
print('세전 연봉:',a,'만원\n세후 연봉:',money(c,b),'만원')
round(100.2)

# 3.
a,d=input('이름과 점수를 입력해주세요.: ').split()
c=0
b=int(d)
if b>=95:
    c='A+'
elif b>=90:
    c='A'
elif b>=85:
    c='B+'
elif b>=80:
    c='B'
elif b>=75:
    c='C+'
elif b>=70:
    c='C'
elif b>=65:
    c='D+'
elif b>=60:
    c='D'
else:
    c='F'
print('학생이름: ',a,'\n점수: ',b,'점','\n학점: ',c)

# 4.
a,b=input('나이와 지불 유형을 적어주세요.: ').split()
while b!='현금' and b!='카드':
    a,b=input('다시 나이와 지불 유형을 적어주세요.: ').split()
c=int(a)
d=0
if 8<=c<14:
    d=450
elif c<20 and b=='현금':
    d=1000
elif c<20 and b=='카드':
    d=720
elif c<75 and b=='현금':
    d=1300
elif c<75 and b=='카드':
    d=1200
else:
    d='무료'
print('나이: ',a,'\n지불능력:',b,'\n버스요금:',d)
