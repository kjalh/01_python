i = -1 # 데이터 넣는 위치 결정

def push(): # 데이터 추가
    global i
    if stack[size-1] != None:   #   스택 전부 채워져 있는지 확인
        return print("\n스택 꽉 차있음, 데이터 삭제 바람\n")
    else:
        data = input("넣고 싶은 데이터 입력: ")
        i += 1  # 데이터 위치 1 증가
        stack[i] = data # 데이터 넣기
        
    print(f"i = {i}")


def pop():  # 데이터 삭제
    global i

    if stack[0] == None:
        i = -1
        return print("스택 비어 있음")
        

    stack[i] = None
    i -= 1

    print(f"i = {i}")
    


size = int(input("스택의 크기: "))

stack = [None] * size 

while True:
    print("-------------------------메뉴-----------------------------")
    print("종료: 0")
    print("추가: 넣")
    print("삭제: 빼")

    data = input("\n입력: ")

    if data == '0':
        break

    elif data == "넣":
        push()
        print()
    elif data == "빼":
        pop()
        print()
    else: 
        print("다시 입력 바람") 
        print()
    
    print(stack)  # 스택 확인 없어도 됨






















