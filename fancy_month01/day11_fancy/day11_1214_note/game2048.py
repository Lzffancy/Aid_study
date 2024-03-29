"""
    2048核心算法
"""
list_merge = [2, 0, 2, 0]

# 1. 定义函数　zero_to_end()
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):  #倒序索引　
        if list_merge[i] == 0:
            del list_merge[i]#有零则删除
            list_merge.append(0)#

zero_to_end()
print(list_merge)


# 2. 定义函数　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
def merge():
    """
        合并数据
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()   #
    for i in range(len(list_merge) - 1):#正序索引
        if  list_merge[i] == list_merge[i + 1]:# 判断是否相同数字
            list_merge[i] += list_merge[i + 1]# 相同则相加给merge[i]
            del list_merge[i + 1]
            list_merge.append(0)

# print(list_merge)

# 3. 向左移动
map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]

def move_left():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        list_merge = line
        # merge内部操作的列表,就是二维列表map中的行
        merge()

# move_left()
# print(map)

# 4. 向右移动 move_right
def move_right():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        # 切片读取数据时产生新列表
        list_merge = line[::-1]
        # 处理的是新列表中数据,不是二维列表的行
        merge()
        # 所以需要还原数据(list_merge --> map)
        line[::-1] = list_merge
        # line = list_merge[::-1] # 错误,修改的是变量line不是map
        # line[:] = list_merge[::-1]


#move_right()
#print(map)

# 5. 向上移动
# 矩阵转置 --> 向左移动 --> 矩阵转置

# 6. 向下移动
# 矩阵转置 --> 向右移动 --> 矩阵转置