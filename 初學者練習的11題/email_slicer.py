address = input("輸入您的Email\n")
inx = 0
start =0
end = 0
for i in address: #走一遍str,找 @ ~ . 的子字串
    #print(i)
    if(i == '@'):
        start = inx+1 #@不包括在字串內
    if(start != 0 and i == '.'):
        end = inx
    inx +=1
#print(type(address))
if(address[start:end] == "gmail"):  #注意是[a:b] not [a,b],不然會跑出TypeError: string indices must be integers
    print(f"這是註冊在 Google 之下的 Email地址")
elif(start != 0 and end !=0):
    print(f"這是註冊在 {address[start:end]} 之下自定義域")#inx start~end-1
else:
    print("你輸入的不是Email")
