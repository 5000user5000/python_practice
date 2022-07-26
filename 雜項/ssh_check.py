#!/usr/bin/env python
import paramiko  #用ssh連線必要的套件


def getIP(output):  #假設output = "Wifi 192.168.7.5" 
    str = output.replace("Wifi","") #把Wifi換成空字串
    str = str.strip() #把字串前後的空格用掉,只留下ip
    return str  # 

# parameter
username = "你的使用者名稱"
password = "密碼"
hostIP = "你要連線的那台電腦的ip" #我是連到ubuntu的vm,內網ip是192.168....


port = 22 #我有嘗試用其他的,但似乎不行


try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostIP, port, username, password, timeout=4)
    
    #輸入指令,並根據回傳的行數來確認是否重啟[W]atchingDog
    stdin, stdout, stderr = client.exec_command('ps aux | grep "[W]atchingDog"') #ps aux | grep ...是linux指令,檢查有無這程序,用[]減少不必要的輸出,所以只要有輸出1行以上表示有該程序存在
    if(len(stdout.readlines() ) >=1):
        print("WatchingDog 已啟動了")
    else:
        print("WatchingDog 尚未啟動")
    
    #如果要檢查多個程序,只要複製上面貼上,修改部分地方就可,不會衝突 
        
    print("==========") #分隔線
    #檢查conf 的 ip 正確與否 
    stdin, stdout, stderr = client.exec_command('cat /opt/xxx/yyy.conf | grep "Wifi" ') #從某個路徑裡的conf裡只抓有Wifi屬性(也可其他)的地方
    thisIP = getIP(stdout.readlines()[0])  #list->string ,所以使用[0]  , 因為原本會是list沒有replace屬性,所以要轉成string,這裡假定我們要的都是在list的第一個
    if(thisIP == "任何你想比對的"):
        print("ip 正確")
    else:
        print("ip 錯誤,請改正")
    
   #如果要檢查多個檔案,只要複製上面貼上,修改部分地方就可,不會衝突 
   
       
    client.close()
    
except Exception:
    print("Exception!!")
    raise


