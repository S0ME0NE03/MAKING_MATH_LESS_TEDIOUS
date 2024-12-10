MAX = input("what is the max you want to go to"
dic = {1:0,2:1}
#print(dic[1])
print(dic[2])
p = 2
i = p
c = i
try:
    while c < MAX:
        i += 1
        p = dic[i - 2] + dic[i - 1]

        dic.update({i : p})
        print(p)
        c = dic[i - 1] + dic[i - 0]
        
except:
    pass
