while True:
    user_input=input("Please say something('q' to quit):")
    if user_input == 'q':
        break
    print(user_input)
    for filter_word in open('C:/Users/17156/Desktop/filtered_words.txt','r',encoding='UTF-8'):
         #这里碰到一个东西就是，使用open()文件迭代器的方法，会自动在读取的对象后面增加一个跨行符号\n ，
         #所以这里需要一个rstrip()去掉右边的跨行符。
        if filter_word.rstrip() in user_input:    
            print('Freedom!')
            break
    else:
        print('Human Rights!')

