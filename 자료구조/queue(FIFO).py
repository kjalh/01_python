
queue = []
i = 0

def enqueue(): # 데이터 추가
    if len(queue) >= last:
        return print("큐가 꽉 차있음, 데이터 삭제 바람")
    else:
        data = input("넣고 싶은 데이터 입력: ")
        queue[i] = data
        i += 1

        print('성공적으로 입력이 들어감')



def dequeue(): # 데이터 삭제

    for 
    pass



last = int(input("큐의 크기를 정해라: "))


while True:
    print("종료: 0")
    print("추가: enqueue")
    print("삭제: dequeue")

    data = input("입력: ")

    if data == '0':
        break

    elif data == "enqueue":
        enqueue()
    elif data == "dequeue":
        dequeue()
    else: 
        print("다시 입력 바람") 
    

