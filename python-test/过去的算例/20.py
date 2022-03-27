def main():
    fish=1
    while True:
        total, enough =fish,True
        for _ in range(5): #if使用次数，不符合则break跳出for循环
            if (total - 1) % 5 == 0:
                total = (total - 1)  //  5 * 4 #在第一次能分好后，改变总数准备下次分鱼
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1 

if __name__ =='__main__': #如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    main()