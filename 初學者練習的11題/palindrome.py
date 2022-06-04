s = input("input any string \n")
tail_index = len(s) - 1
head = 0
while head < tail_index:
    if s[head]!= s[tail_index]:
        print("非回文")
        exit(0) #直接停止,加快速度
    head+=1
    tail_index-=1

print("此為回文")
#dsa hw3有更高階的問題
