import sqlite3
import os

def getAllTable(cursor,table_name:list):
    """取得所有表格名稱

    Args:
        cursor (Cursor): 游標物件
        table_name (list): 表格名稱
    """
    cursor.execute(f"select name from sqlite_master where type='table' order by name;")
    records = cursor.fetchall() #取得回傳資料
    for i in records:
        table_name.append(i[0])
    
def clear_txt(txt_path):
    """清空txt檔內之前的內容,避免和新寫入的疊加在一起

    Args:
        txt_path (str): 欲清空的文檔位置
    """
    with open(txt_path,'r+') as data:
        data.truncate(0)
 

def printFunc(name,cursor,f):
    """把欄位組合成code寫入txt

    Args:
        name (str): 表格名稱
        cursor (Cursor): 游標物件
        f (TextIOWrapper): 開啟的txt
    """
    cursor.execute(f'PRAGMA table_info([{name}]);')
    records = cursor.fetchall() #取得回傳資料
    #print(records)
    #print("record type => ", type(records)) #回傳資料型態
    f.write(f"void My{name}() \n")
    f.write('{\n')
    f.write(" 任何你要用的程式;\n")
    for i in records:
        #print("屬性 => ", i[1]) #[1]是我這裡讀到的屬性,不一定是這個,先print records看看
        f.write(f" ... _T(\"{i[1]}\")...\n")
    f.write(f"  len = {len(records)};\n")
    f.write('}\n')
if __name__ == '__main__':
    DataPath = os.path.join(os.getcwd(),"xxx.db")#也可直接呼叫xxx.db,當db和py檔放一起時
    #print(DataPath)
    conn = sqlite3.connect(DataPath) #建立連線
    cursor = conn.cursor() #取得游標物件
    
    table_name =[]
    getAllTable(cursor,table_name) #python很方便,不像c那樣得用指標才能修改table_name
    
    #先清空(不需join)
    clear_txt('data.txt')
    #打開txt
    f = open('data.txt','w')
    #把資訊寫入txt   
    for name in table_name:
        printFunc(name,cursor,f)
    #關掉
    f.close()
