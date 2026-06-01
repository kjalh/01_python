class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = size - 1
        self.idx = 0


    def push(self):
        if None not in self.stack:
            print(self.stack)
            self.idx = self.size
            return print("꽉참")
        
        d = input("입력 값: ")
        
        
        if self.idx >= 0 and self.idx <= self.size:
            self.stack[self.idx] = d
            self.idx += 1

            if self.idx >= self.size:
                self.idx = self.size

            print(self.stack)
            return print("입력 됨")



    def pop(self):

        if self.idx <= self.size and self.idx >= 0:
            self.idx -= 1
            self.stack[self.idx] = None
            

            if self.idx < 0:
                self.idx = 0
            
            print(self.stack)
            return print("빠짐")










stack = Stack(int(input("크기: ")))



while True:
    p = input("push/pop : ")
    
    if p == "push":
        stack.push()
    elif p == "pop":
        stack.pop()
    elif p == "0":
        exit()
    else:
        print("다시 입력")

