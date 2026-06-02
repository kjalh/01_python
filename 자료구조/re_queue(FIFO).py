class Queue:   
    def __init__(self, size):       # 생성자 
        self.size = size            # 큐 크기 받기
        self.queue = [None] * (size + 1) # 큐 크기 지정 + 1은 하나 크게 만들어서 빼기 쉽게 
        self.idx = 0                # 이 위치에 넣기

    

    def enqueue(self, in_data):
        if self.idx >= self.size:       # 빈 큐인지 확인
            self.idx = self.size        # 더이상 증가 안 되게 
            return print("\n입력 실패 꽉 참")
        
        self.queue[self.idx] = in_data  # 큐에 데이터 넣기
        self.idx += 1                   # 다음 큐에 넣기 위해 idx(위치) 1wmdrk

        print(self.queue)               # 큐에 제대로 들어갔는지 시각적 자료



    def dequeue(self): 
        if self.idx == 0:               # 빈 큐 확인
            return print("빈 큐")

        j = 0                           # 반복문에 쓰일
        while True if self.queue[j] != None else False:   # 해당 위치에 값이 있어야 True
            self.queue[j] = self.queue[j+1]   # 뒤에 있는 값을 하나씩 앞으로 이동
            j += 1                      # j로 인덱스 확인

        self.idx -= 1                   # 넣을 위치 -1
        if self.idx <= -1:              # 넣을 위치가 -1 이하가 되지않도록 확인
            self.idx = 0
        print(self.queue)               # 큐에서 제대로 빠졌는지 시각적 자료


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