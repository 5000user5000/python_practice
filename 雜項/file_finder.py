import time
import os
import sys
from datetime import datetime

"""
執行方法範例:
python ./file_finder.py 7 D:/
意思是會print D槽下所有7天內有做修改的檔案。

打包成exe:
terminal上輸入
pyinstaller --onefile file_finder.py
這樣就會打包成exe檔，可以直接點擊執行，如果被防毒軟體抓了，可以加入白名單。
記得要先寫死時間和讀取的檔案路徑。例如:getFile(7,"D:\NOTE")，並把 sys.argv的部分註解掉。

User Story:
身為一個時常寫文件的人，我每週得定期上傳某檔案夾下的有做變更的文件去做備份，
檔案一多,就會需要有這樣的程式去做搜尋。
之後再補自動上傳到Google Drive的代碼。不過變動文件不多的話，還是直接手動上傳就好。
"""


#想取得的時間範圍
time_before = sys.argv[1]

#欲取的路徑
path = sys.argv[2]

#取得時間範圍的文件
def getFile(time_before,path):
    now = time.time()#當前時間戳
    past = now - time_before*86400 #例如回到7天前的文件,就用時間戳去減掉7天的秒數 #好處是不用在使用月份轉換時間

    #遍歷文件夾 , 用os.listdir只能取得當前檔案,不能取得子目錄的檔案
    for  root,dirs,files in os.walk(path):
        for f in files:
            t = os.path.getmtime(f'{root}\{f}')
            if t > past:
                print(f"File: {root}\{f} , Modified: {datetime.fromtimestamp(t)}")

if __name__ == '__main__':
    getFile(time_before,path)
    waitKey = input("Press any key to exit...")

