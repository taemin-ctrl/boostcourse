#1

korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"

chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

def king(korea_king, chosun_king):

    dic1={} #고려의 딕션너리

    dic2={} #조선의 딕셔너리

    count=0 #조선과 고려에 모두 있는 왕의 수

    a=korea_king.split(',')

    b=chosun_king.split(',')

    for i in range(len(a)): 

        dic1[a[i]]=a[i]

    for j in range(len(b)):

        dic2[b[j]]=b[j]

    for i in b:

        if i in dic1:

            print('조선과 고려에 모두 있는 왕: ' ,dic1[i])

            count+=1

    print(f'조선과 고려에 모두 있는 왕 이름은 총 {count}입니다.')

king(korea_king, chosun_king)

#2 

def sales_management(member_names, member_records):

    dic={} #실적 평균

    lis=[] #정렬 리스트

    for i in range(0,len(member_names)):

        dic[member_names[i]]=sum(member_records[i])/len(member_records[i])

    for k,v in dic.items():

        lis.append((v,k))

    lis=sorted(lis,reverse=True)

    for j in range(0,2):

        if (lis[j])[0]>5:    

            print(f'보너스 대상자 {(lis[j])[1]}')

    lis=sorted(lis)

    for j in range(0,2):

        if (lis[j])[0]<=3:    

            print(f'면담 대상자 {(lis[j])[1]}')

member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]

member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 

           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],

           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

sales_management(member_names, member_records)

#3 

stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"

sells = [82000, 160000, 835000, 410000]

a=stocks.split(',')

b=[] 

for i in a:

    b.append(i.split('/'))

dic={}

for i in range(0,4):

    dic[(b[i])[0]]=(sells[i]-int((b[i])[2]))/int((b[i])[2])*100

lis=[]

for k,v in dic.items():

    lis.append((v,k))

lis=sorted(lis, reverse=True)

for i in range(0,4):

    print(f'{(lis[i])[1]}의 수익률 {(lis[i])[0]:.3}')

#4 

info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

def good_customer(info):

    dic={}

    a=[]

    a=info.split(',')

    b=[]

    c=[]

    d=[]

    e=[]

    f=[]

    g=[]

    for i in range(0,6):

        b.append(a[6*i])

        c.append(a[6*i+1])

        if a[6*i+2]=='x':

            d.append('010-0000-0000')

        else:

            d.append(a[6*i+2])

        e.append(a[6*i+3])

        f.append(a[6*i+4])

        g.append(a[6*i+5])

    dic['아이디']=b

    dic['나이']=c

    dic['전화번호']=d

    dic['성별']=e

    dic['지역']=f

    dic['구매횟수']=g

    print(dic)

    for j in g:

        if int(j)>=8:

            if d[g.index(j)]!='010-0000-0000':

                print(f'아이디: {b[g.index(j)]} 나이: {c[g.index(j)]} 전화번호: d[g.index(j)] 성별: e[g.index(j)] 지역: f[g.index(j)] 구매횟수 g[g.index(j)]')

            

good_customer(info)

#아이디,나이,전화번호,성별,지역,구매횟수
