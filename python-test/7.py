#通过自定函数判断字符串是否为数字
def is_number(self): #这应该是复函数
    try: #如果能执行float()语句，字符串self为浮点数
        float(self)
        return True
    except ValueError:
        pass

    try:  
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(self)
        return True
    except (TypeError,ValueError):
        pass
    
    return False #初级判断到这里结束

    
# 测试字符串和数字
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True
 
# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # Falsechuji


    