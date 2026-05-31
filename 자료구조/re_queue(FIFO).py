class Queue:   
    def __init__(self, size):
        self.size = size
        self.queue = [None] * (size + 1)
        self.idx = 0

    


    def enqueue(self, in_data):
        if self.idx >= self.size:
            self.idx = self.size
            return print("\n입력 실패 꽉 참")
        
        self.queue[self.idx] = in_data 
        self.idx += 1

        print(self.queue)



    def dequeue(self): 
        if self.idx == 0:
            return print("빈 큐")

        j = 0
        while True if self.queue[j] != None else False:
            self.queue[j] = self.queue[j+1]
            j += 1

        self.idx -= 1
        if self.idx <= -1:
            self.idx = 0
        print(self.queue)


size = int(input("큐의 크기: "))
r_queue = Queue(size)

while True:
    print("-------------------------메뉴-----------------------------")
    print("종료: 0")
    print("추가: 넣")
    print("삭제: 빼")

    data = input("\n입력: ")

    if data == '0':
        exit()

    elif data == "넣": 
        r_queue.enqueue(input("입력 값: "))
        print()
    elif data == "빼":
        r_queue.dequeue()
        print()
    else: 
        print("다시 입력 바람") 
        print()