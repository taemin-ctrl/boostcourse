1.시스템 유틸리티 제작, GUI 프로그래밍, 웹 프로그래밍, 수치연산 프로그래밍, 데이터베이스 프로그래밍, 데이터 분석, 사물인터넷 등.
저는 파이썬 배워서 전공 공부을 매진하고 싶습니다.
2. CPU: 컴퓨터의 정중앙에서 모든 데이터를 처리하는 장치(두뇌에 해당)
main memory: CPU가 실행할​ 프로그램과 데이터를 저장하는 기억장치
secondary memory: 컴퓨터의 CPU에 직접 연결된 주기억장치가 아닌 디스크, 테이프 등 외부의 기억장치를 지칭
3.#1. 1/'1'-typeerror
1/1
#2. int('asd')-valueerroe
int(5)
#3. if 1==1
#print(1)-syntaxerror
if 1==1:
    print(1)
#4. ant- nameerror
ant=1
a=[0,1,2]
#5. a[5]-indexerror
a[1]
#6. 1/0-zerodivisionerror
1/1
4.age=int(input('당신의 나이는 몇살입니까?:'))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
while birth != 0 and birth != -1:
   birth = int(input("다시 입력해주세요. 맞으면 0 아니면 -1 : ")) 
print('당신은 미국 나이는 ',age+birth-1,'살입니다.')
