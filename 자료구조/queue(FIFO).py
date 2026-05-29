

i = 0

def enqueue(): # 데이터 추가
    global i

    if queue[size-1] != None:
        return print("\n큐가 꽉 차있음, 데이터 삭제 바람\n")
    else:
        data = input("넣고 싶은 데이터 입력: ")
        queue[i] = data

        i += 1
        print(queue)
        print('성공적으로 입력이 들어감')



def dequeue(): # 데이터 삭제
    global i
    if queue[0] == None:
        return print("큐가 비어있음")
    
    print(f"1번 제거 {queue[0]}")


    for j in range(0, i-1): # 4    0 1 2 3
        queue[j] =  None
        queue[j] = queue[j+1]
        queue[j + 1] = None


        # queue[j] = None
        # queue[j] = queue[j+1]
        # queue[j+1] = None

    i -= 1
    print(queue)



size = int(input("큐의 크기: "))

queue = [None] * size 


while True:
    print("종료: 0")
    print("추가: 넣")
    print("삭제: 빼")

    data = input("입력: ")

    if data == '0':
        break

    elif data == "넣":
        enqueue()
    elif data == "빼":
        dequeue()
    else: 
        print("다시 입력 바람") 
    

