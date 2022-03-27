people={}
for x in range(1,31):
    people[x]=1
    print(people[x])
check=0
i=1
j=0
while i<=31:
    if i == 31: #重新开始
        i=1
    elif j == 15: #结束设定
        break
    else:
        if people[i] == 0: #跳过下船的人
            i+=1
            continue
        else:   #下船条件
            check+=1
            if check == 9:
                people[i]=0
                check = 0
                print("{}号下船了".format(i))
                j+=1
            else:
                i+=1
                continue