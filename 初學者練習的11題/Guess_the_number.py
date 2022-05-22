import random
#電腦隨機找1~50中一個數
computer = random.randint(1,50)#1~50隨機整數變數
# 猜測次數,從1開始
times = 1 
#print(str(computer)) #用來確認code有無跑對,把電腦的數顯示出來

while True:
    player = int(input("Guess a number 1~50:"))
    if player == computer:
        print("Right!")
        print(f"You have guessed {times} times")
        break
    else:
        if computer<player:
            print("Too big!")
        else:
            print("Too small!")
        willing = int(input("Want to play again? y:1 n:0 "))
        if willing == 0:
            break
        #else就免了,直接繼續跑
        times += 1 #次數+1

#關於輸出格式參考 https://medium.com/tsungs-blog/python-%E5%AD%97%E4%B8%B2%E6%A0%BC%E5%BC%8F%E5%8C%96-fdfe4ac41a2d
