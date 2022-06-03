#定義一個取縮寫的func (網路上的方法)
def acronym(phrase):
    L = phrase.split()
    result = ""
    for i in L:
        result += i[0].upper() #加在string裡這樣輸出每一個字元才不會跳行,upper()是轉大寫
    return result

s = input("input any sentence \n")
result = acronym(s)
print(result)

#我原本是想用s.split() -> for i in s:print(i[0]),不知為何輸出全文
# 因為s.split()並不會改變s內容,必須把它指定給某個變數才行
# input : as soon as possible
# s = as soon as possible
# h = ['as', 'soon', 'as', 'possible']
'''
# my ver

s = input("input any sentence \n")
h = s.split()
for i in h:
    print(i[0].upper())
'''

