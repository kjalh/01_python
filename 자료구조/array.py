class Array:
    def __init__(self, size):   # 생성자
        self.size = size        # 배열 크기 지정
        self.array = [None] * size


    def data_in(self, data): # 데이터 추가 데이터가 추가될 때 값이 뒤로 밀려나기
        if None not in self.array:      # 배열 전부 차있으면 실행ㅇ
            return print("\n데이터 삭제 바람")
        
        if data in self.array:      # 중복 값 입력 안 되게
            return print("\n이미 안에 있음")
        
        w = input("원하는 위치?(o, x) : ")

        if w == 'x':
            for i in range(self.size): # 반복문으로
                if self.array[i] == None:   # None을 찾아서    (마지막 위치에)
                    self.array[i] = data    # 값을 넣음
                    break
            
        elif w == 'o':
            idx = int(input("위치(1번은 0번부터) : ")) 

            if idx < 0 or idx >= self.size: # 입력값 배열 범위 확인
                return print("범위 초과")

            if self.array[idx] != None: # None이 아니면 실행
                for i in range(self.size - 1, idx, -1): # 오른쪽으로 하나씩 이동
                    self.array[i] = self.array[i-1]

            self.array[idx] = data # 원하는 인덱스에 넣기

        print(self.array) # 배열 확인



    def data_out(self, idx): # 데이터 삭제 해당 데이터가 삭제되면 뒤에 있는 값들은 하나씩 앞으로
        if idx >= self.size - 1:    # 배열 마지막부터 범위를 벗어나도 마지막 값 뺌
            self.array[self.size-1] = None
            print("맨 뒤 뺌")
        else:
            for i in range(idx, self.size - 1): # 원하는 값 지우고 그 기준까지 배열 왼쪽 앞으로 이동
                self.array[i] = self.array[i+1]

            self.array[self.size-1] = None  # 마지막 값에 None 넣어주기

        print(self.array) # 배열 확인

    



    def data_find(self, data):  # 데이터 조회

        if data in self.array:      # 배열 안에 값이 있는지 먼저 확인
            for i in range(self.size):  # 있으면 몇 번째에 있는지 반복문 돌리기
                if self.array[i] == data:   # 원하는 값 찾으면 멈추기
                    return print(f"인덱스 {i}번에 {data} 있음")
        else:
            return print("안에 없음")
        


size = int(input("배열 크기: "))
ba = Array(size)

while True:
    print("-------------------------메뉴-----------------------------")
    print("종료: 0")
    print("추가: 넣")
    print("삭제: 빼")
    print("조회: 조")

    data = input("\n입력: ")

    if data == '0':
        exit()
    elif data == "넣": 
        ba.data_in(input("입력 값 : "))
        print()
    elif data == "빼":
        idx = int(input("위치(인덱스 0부터) : "))
        ba.data_out(idx)
        print()
    elif data == "조":
        ba.data_find(input("조회 값: "))
    else: 
        print("다시 입력 바람") 
        print()