#1
def make_comma(a):
    if len(a)%3==1:
        b=a[0:1]
        for i in range(1,len(a),3):
            b+=','+a[i:i+3]
    elif len(a)%3==2:
        b=a[0:2]
        for i in range(2,len(a),3):
            b+=','+a[i:i+3]
    else:
        b=a[0:3]
        for i in range(3,len(a),3):
            b+=','+a[i:i+3]
    return(b)
b=input('숫자를 입력해주세요.: ')
print(make_comma(b))

#2
def count_word(a, b):
    count=0
    for i in range(0,len(a)-len(b)+1):
        if a[i:i+len(b)]==b:
            count+=1 
    f = open('txt','w')
    f.write(b)
    f.close()    
    print(count)    
a,b=(input('파일과 찾고 싶은 글자를 적어주세요.:')).split(',')
count_word(a, b)

#3-1
def wrong_guest_book(guest_book):
    a,b,c,d,e=guest_book.split('\n')
    if a[3:6]!='010' or a[11:12]!='-' or a[6:7]!='-' or len(a)!=16:
        print('잘못 쓴 사람:',a[0:2])
        print('잘못 쓴 번호:',a[3:] )
    if b[3:6]!='010' or b[11:12]!='-' or b[6:7]!='-' or len(b)!=16:
        print('잘못 쓴 사람:',b[0:2])
        print('잘못 쓴 번호:',b[3:] )
    if c[3:6]!='010' or c[11:12]!='-' or c[6:7]!='-' or len(c)!=16:
        print('잘못 쓴 사람:',a[0:2])
        print('잘못 쓴 번호:',a[3:] )
    if d[3:6]!='010' or d[11:12]!='-' or d[6:7]!='-' or len(d)!=16:
        print('잘못 쓴 사람:',d[0:2])
        print('잘못 쓴 번호:',d[3:] )
    if e[3:6]!='010' or e[11:12]!='-' or e[6:7]!='-' or len(e)!=16:
        print('잘못 쓴 사람:',e[0:2])
        print('잘못 쓴 번호:',e[3:] )
    f = open('101','w')
    f.write(guest_book)
    f.close()
book='김갑,123456789\n이을,010-1234-5678\n박병,010-5678-111 \n최정,111-1111-1111\n정무,010-3333-3333'
wrong_guest_book(book)

#3-1-1
def wrong_guest_book(guest_book):
    b,c,d,e,f=guest_book.split('\n')
    lis=[b,c,d,e,f]
    for a in lis:
        if a[3:6]!='010' or a[11:12]!='-' or a[6:7]!='-' or len(a)!=16:
            print('잘못 쓴 사람:',a[0:2])
            print('잘못 쓴 번호:',a[3:] )
    fil = open('101','w')
    fil.write(guest_book)
    fil.close()
book='김갑,123456789\n이을,010-1234-5678\n박병,010-5678-111 \n최정,111-1111-1111\n정무,010-3333-3333'
wrong_guest_book(book)

#3-2
def wrong_guest_book(guest_book): 
    f = open('101','w')
    f.write(guest_book)
    f.close
    f = open('101','r')
    for _ in range(0,4):
        s=f.readline()
        g=s.rstrip('\n')
        if g[3:6]!='010' or g[11:12]!='-' or g[6:7]!='-' or len(g)!=16:
            print('잘못 쓴 사람:',g[0:2])
            print('잘못 쓴 번호:',g[3:])   
book='김갑,123456789\n이을,010-1234-5678\n박병,010-5678-111\n정무,010-3333-3333'
wrong_guest_book(book)

#4
def check_id(a):
    if len(a)!=13:
        print('잘못된 번호입니다.')
    else:
        print(a[0:6]+'-'+a[6:14])
        if '00'<=a[0:2]<='21':
            b=input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x :')
            if b=='o'and a[6:7]=='3' or '4':
                if a[6:7]=='3':
                    gender='남자'
                else:
                    gender='여자'
                print(a[0:2]+'년',a[3:4]+'월',d)    
            elif b=='x' and a[6:7]=='1' or '2':
                if a[6:7]=='1':
                    gender='남자'
                else:
                    gender='여자'
                print(a[0:2]+'년',a[3:4]+'월',gender)
            else:
                print('잘못된 번호입니다.')
a=input('주민번호를 입력해주세요.:')
check_id(a)
