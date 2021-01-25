"""
    Python 高级
        一.程序结构
            1.物理结构
                根目录
                    mina.py
                    包
                        模块
                            类
                                方法(函数)
                                    语句
            2.根目录:主模块所在文件夹
            3.主模块:第一次运行的模块
            4.sys.path:系统路径
                导入模块是否成功的唯一标准:
                导入路径 + 系统路径 = 真实路径
            5.导入方式
                import 模块
                from 模块 import 成员
                    注意:命名冲突
            5. 导入包
                import 包
                from 包 import 包
                在包的__init__.py文件中进行配置
        二. 异常处理
            价值:让程序按照既定流程执行
            本质:快速传递错误消息
            原则:就近处理
            手段:
                try:
                    可能发生错误的代码
                    # 发送错误消息
                    raise 异常类(数据)
                    # 接收错误消息
                except 异常类型 as 变量:
                    pass
        三. 生成器
            1. 生成器函数
                创建
                    def 函数名():
                        ...
                        yield 数据
                        ...

                使用
                    for item in 函数名():
                        # for内部用next调用函数

                    容器名(函数名())

            2.生成器表达式
                (for 变量 in 可迭代对象 if 条件)
            3.传统思想与生成器思想
                传统:使用容器将数据存在内存中操作
                    优点:操作灵活(索引,切片,反复,修改)
                    缺点:占用内存过多
                生成器:惰性操作/延迟操作(循环一次计算一次返回一次)
                    优点:几乎不占内存
                    缺点:操作不灵活(从头到尾读取一次)
                    解决:容器名(函数名())
            4.结论:函数返回单个结果使用return
                         多         yield

        四.迭代器
            1. 框架
                class 可迭代对象:
                    def __iter__(self):
                        return 迭代器()

                class 迭代器:
                    def __next__(self):
                        return 数据

                for 变量 in 可迭代对象():
                    print(变量)
            2. 作用
                使用者只需通过一种方式(for)，
                便可简洁明了的获取聚合对象中各个元素，
                而又无需了解其内部结构。

        五.函数式编程
            1. 函数作为参数:能够传递判断条件,处理逻辑

            2. 函数作为返回值:能够逻辑连续
                外函数接收旧功能,内函数重复使用旧功能

            3. 装饰器
                def 装饰器名称(旧功能)
                    def 包裹函数():
                        新功能
                        旧功能()
                    return 包裹函数
"""