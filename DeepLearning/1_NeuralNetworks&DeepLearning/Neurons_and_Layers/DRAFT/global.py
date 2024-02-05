# 定义一个全局变量
# counter = 0

def increment_G_counter():
    global counter  # 指明我们要使用的是全局变量counter
    counter += 1    # 增加全局变量counter的值
    print("Global Counter: \n", counter)
    
# def increment_L_counter():
#     counter += 1    # 增加全局变量counter的值
#     print("local Counter: \n", counter)


def print_counter():
    print("Counter:", counter)

# Main Function
if __name__ == '__main__':
    counter = 8
    print("function counter: ",counter)
    # increment_L_counter()

    increment_G_counter()
    
    print("Function counter2: ",counter)