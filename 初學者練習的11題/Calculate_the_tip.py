people = int(input("有多少人?\n"))#不轉成int就無法計算,注意不是(int),而是int()
print("各自餐費多少錢?")
fee = []#list,動態陣列,c的話要用指標+malloc才行
sum = 0
for i in range(people):
    fee.append( int(input()) )
    sum += fee[i]
print(f"一共是{sum}元!")#print不用特別加\n,但input要
order = input("請問是一起結帳嗎?(Y/N)\n")
if order == 'Y':
    tip = round(sum/10) #round是內建的四捨五入,不用多加int()
    print(f"在費率 10% 的狀況下，小費為 {tip}，總金額 {sum+tip}")
else:
    print("在費率 10% 的狀況下")
    for i in range(1,people+1): #客人從1開始數,1~people
        tip = round(fee[i-1]/10) #fee從0開始,不然會出界
        print(f"客人{i}，小費為 {tip}，總金額 {fee[i-1]+tip}")


