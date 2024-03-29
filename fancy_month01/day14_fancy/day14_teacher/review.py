"""
    复习
    一、Python程序结构
    根目录
         包
                模块
                        类
                             函数(方法)
                                        语句
         main.py
    1. 根目录：主模块所在文件夹
    2. 主模块：第一次执行的文件
    3. 系统路径sys.path：导入模块的搜索路径
    4. 导入成功的唯一标准：导入路径 + 系统路径 = 真实路径

    二、导入方式
    1. "我过去"：使用变量关联目标模块地址
       import 模块
       模块.成员

    2. "你过来"：将目标模块成员加入到当前模块作用域中
       小心命名冲突
       from 模块 import 成员
       直接使用成员

    3. 直接导入包，必须在包的__init__.py文件中进行配置
"""