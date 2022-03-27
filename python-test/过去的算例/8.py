#判断一个数字是否为奇数或偶数
#加入判断为整数
'''
while True: #死循环
    try:
        num=int(input("input a number:"))
    except ValueError:
        print('input erro')
        continue
    
    if (num%2)==0:
        print('%d is 偶数' %num)
    else:
        print('%d is 奇数' %num)
    break #continue 跳出本循环，break跳出所有循环
'''

#simple and short
num=eval(input('input number:'))
print('{} is'.format(num)+(' even number.'if num%2==0 else' odd number.'))