i = 0      # 데이터 넣는 위치 결정

def enqueue(): # 데이터 추가
    global i

    if queue[size-1] != None:   #   큐 전부 채워져 있는지 확인
        return print("\n큐가 꽉 차있음, 데이터 삭제 바람\n")
    else:
        data = input("넣고 싶은 데이터 입력: ")
        queue[i] = data # 데이터 넣기

        i += 1  # 데이터 위치 1 증가
        if i >= size:
            i = size - 1
        




def dequeue(): # 데이터 삭제
    global i
    if queue[0] == None:    # 큐 비어 있는지 확인
        return print("큐가 비어 있음")
    
    print(f"1번 제거 {queue[0]}")
    
    j = 0   # 반복문에 쓸 j 선언
    while True if j != None else False: # 뒤에 있는 데이터를 앞으로 옮기는 작업
        if j < size - 1 :
            queue[j] = queue[j+1]   # 뒤에 있는 데이터를 앞으로 옮기는 작업
            queue[j+1] = None       # 값을 뺄 때 마지막 값에 None을 넣어줌
            j += 1
            
            i -= 1
            if i < 0:
                i = 0





size = int(input("큐의 크기: "))

queue = [None] * size 

while True:
    print("-------------------------메뉴-----------------------------")
    print("종료: 0")
    print("추가: 넣")
    print("삭제: 빼")

    data = input("\n입력: ")

    if data == '0':
        break

    elif data == "넣":
        enqueue()
        print()
    elif data == "빼":
        dequeue()
        print()
    else: 
        print("다시 입력 바람") 
        print()
    
    print(queue)  # 큐 확인 없어도 됨
