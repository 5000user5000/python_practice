print("請選擇一首歌(輸入序號)")
#song = {"1.Bad Apple","2.華鳥風月","3.どうして"} {}(dict)這樣的話,for loop輸出會順序不斷跳動,非123這樣
song = ["1.Bad Apple","2.華鳥風月","3.どうして"]
for i in song:
    print(i)
#f = open('lyrics.txt', 'r') 會出錯
order = int(input())

#讀取txt檔
import os

absFilePath = os.path.abspath(__file__) #取得絕對路徑,到這個程式執行檔 
path, filename = os.path.split(absFilePath)
path = path + "\lyrics.txt"
f = open(path, 'r',encoding="utf-8")#encoding="utf-8"這樣才能解讀非英文的語言

lines = f.readlines()
lyrics = []
break_point = [] #文檔我用...分割,當讀到分割處(也是節省符號,畢竟歌詞還是別全截),紀錄行數,之後就能取用此行數間的歌詞.如果不想用...,可以去查ascii code from 0x21,用些不會顯示的字符(0x20之類的)
i = 0
break_point.append(i)
for line in lines:
    lyrics.append(line)
    i+=1
    if(line == "...\n"):
        break_point.append(i)      
    #print(line)
f.close()
#print(lyrics)
#print(break_point)
for line in lyrics[ break_point[order-1]:break_point[order]]: #range start~end,但只輸出inx start+1~end,除非start==0,才會輸出 start~end,如此一來,歌詞的開頭不會是"..."
    print(line)

'''
查找檔案的方法
import os
wd = os.getcwd() #現在的路徑(非py檔的上一個檔案夾,而是更大的檔案夾)
print("working directory is ", wd)

filePath = __file__
print("This script file path is ", filePath)

absFilePath = os.path.abspath(__file__)
print("This script absolute path is ", absFilePath)

path, filename = os.path.split(absFilePath)
print("Script file path is {}, filename is {}".format(path, filename))
'''
