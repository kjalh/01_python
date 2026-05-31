i = 0      

def enqueue(): 
    global i

    if queue[size-1] != None:   
        i = size - 1
        return print("\n큐가 꽉 차있음, 데이터 삭제 바람\n")
    else:
        
        data = input("넣고 싶은 데이터 입력: ")

        queue[i] = data 
        i += 1  

        if i >= size:
            i = size - 1
        print(f"i = {i}")
        




def dequeue(): 
    global i
    if queue[0] == None:    
        return print("큐가 비어 있음")
    
    print(f"1번 제거 {queue[0]}")
    
    j = 0   # 반복문에 쓸 j 선언

    while queue[j+1] != None:
        if j < size - 1 :
            queue[:] = queue[1:]   
            if j == size - 1:
                queue[-1] = None    
            j += 1
        else:                       
            break
    
    i -= 1

    if i < 0:
        i = 0

    print(f"i = {i}")





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
