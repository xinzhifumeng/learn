#判断闰年
while True:
    try:
       year=int(input('year:'))
    except:
        print('input erro')
        continue
    if (year%4)==0:
        if (year%100)==0:
            if (year%400)==0:
                print('{} 是闰年'.format(year))
            else:print('{} 不是闰年'.format(year))
        else:print('{} 是闰年'.format(year))
    else:print('{} 不是闰年'.format(year))
    break