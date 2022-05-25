import csv
import string
import os


path = os.path.abspath(".") #找到當前的絕對路徑,但是編輯器的路徑,和.py不太同

translator = str.maketrans('', '', string.punctuation)

word_count = {}
#不是輸入而是讀檔,encoding="utf-8"是我多加的,確定編碼法,否則容易回傳無法decode
text = open(path+'\py works\practice\declare.txt',encoding="utf-8").read() # d:\\...\\python\py works\practice\declare.txt

#根據空格分拆,words為陣列
words = text.split()

#根據每個詞去統計,中文無法解碼
for word in words:
    word = word.translate(translator).lower() #全部轉小寫,這樣Are = are
    count = word_count.get(word, 0) #尋找ondex == word的地方,把之前累計的count拿出來
    count += 1
    word_count[word] = count #可以用非數字做index

#sort,常出現的排最前面,打印前10個
word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

#將資料寫入
output_file = open('words.csv', 'w') #會自動在python folder下生成csv檔
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word_count[word]])

# 關於讀檔和寫入 https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-bf0648108581
# 讀檔路徑設定 https://medium.com/@PatHuang/%E5%88%9D%E5%AD%B8python%E6%89%8B%E8%A8%98-1-%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86-%E7%9B%B8%E5%B0%8D-%E7%B5%95%E5%B0%8D%E8%B7%AF%E5%BE%91-%E8%B3%87%E6%96%99%E9%81%B8%E5%8F%96-1a081fc38e56
# 難度偏高一點,有一些資料結構和讀寫外部檔案
