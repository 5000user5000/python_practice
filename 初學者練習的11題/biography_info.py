#讀檔
import os
from tracemalloc import stop

absFilePath = os.path.abspath(__file__) #取得絕對路徑,到這個程式執行檔 
path, filename = os.path.split(absFilePath)
path = path + "\\touhou_data.txt" #這個要雙斜線
f = open(path, 'r',encoding="utf-8")#encoding="utf-8"這樣才能解讀非英文的語言

lines = f.readlines()
people_info = []

for line in lines:
    people_info.append(line)    
    #print(line)
f.close()

#輸入欲查之人
wanted = input("輸入要找的人\n")
times = 0 #紀錄當下inx,之後才能output相關資料
for i in people_info[::3]: #step = 3
    name = "姓名:"+ wanted+'\n' #每一行後面都會加\n
    #print(name)
    #print(i)
    if( i == name ):
        print(i)
        print(people_info[times+1])
        print(people_info[times+2])
        exit() #結束程式
    times+=3 #因為一次跨三人
