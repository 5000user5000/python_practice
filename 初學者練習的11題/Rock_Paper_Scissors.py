import random
computer = random.randint(1,3)#1~3隨機整數變數
#print(str(computer))#轉成str才能打印
#感覺沒法宣告成int player好怪
player = int(input("1 for scissor ,2 for rock ,3 for paper:"))
#先處理平手
if computer == player:
    print("Draw!")
elif computer - player == -1 or computer - player == 2 : #比對一下就知道,沒必要把所有case窮舉
    print("You Win!")
else:
    print("You Lose!")
