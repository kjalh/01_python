

i = 0

def enqueue(): # 데이터 추가
    global i
    if len(queue) >= last:
        return print("\n큐가 꽉 차있음, 데이터 삭제 바람\n")
    else:
        data = input("넣고 싶은 데이터 입력: ")
        queue.append(data)
        #queue[i] = data
        i += 1


        print(queue)
        print('성공적으로 입력이 들어감')



def dequeue(): # 데이터 삭제
    global i
    if len(queue)<1:
        return print("큐가 비어있음")
    
    print(f"1번 제거 {queue[0]}")


    for j in range(i-1): # 4    0 1 2 3
        queue[j] = queue[j+1]
        #queue[:] = queue[:-1]
    
    i -= 1
    print(queue)



last = int(input("큐의 크기를 정해라: "))

queue = []


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
    

