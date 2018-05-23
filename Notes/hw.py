# -*- coding: utf-8 -*-
'''
第一个程序：Hello, world!
'''
# 单行注释
print('hello, world!')
'文档注释'
print('hello, Python!')

"""
# ********************* 语法与句法1 ************************

* 注释： 四种方式

    单行注释： #
    多行注释：匹配的三个双引号 或者 匹配的三个单引号
    文档字符串注释：代码中单独的字符串

* 续行符： \

    注意：在使用闭合操作符(如小括号，中括号，花括号)以及是三引号包括下的字符串时，不用反斜线也可以直接跨行, 
         但在非三引号字符串中，是需要反斜杠跨行的，如'Hello world'要跨行写的话，要写成'Hello \
         world"

* 一行多语句书写： 利用分号";"隔开

* 代码块用缩进的方式体现

* 代码块用冒号":"分离头与体

* python文件以模块的形式组织

* 标准算术操作符：  +-   *   /   //(地板除)    %    **

* 位操作符： ~(取反)   &(按位与)   |(按位或)   ^(异或) [注意：位操作符只用于整型]

* 标准比较操作符：  >    >=    <    <=    ==    !=

* 逻辑操作符： and   or   not

    注意：python中支持如下的写法：3<4<5,其意义为3<4 and 4<5

* 合法的标识符： 字母+数字+下划线，字母不能为首(和其它语言一样)

* 关键字： 

    查看方式：import keyword; keyword.kwlist
    判断是否是关键字：import keyword; keyword.iskeyword("and")
    
    注意：关键字的说明可见网页[1,2]
                    

* 内建(built-in)名字集合: 可以在任何一级代码使用的名字集合，这些名字可以解释器直接使用，最好不要覆盖使用它们

    注意： built-in是__builtins__模块的成员，是由解释器自动导入的

* 常用的内建函数： https://docs.python.org/3/library/functions.html
"""

print(3<4<5)

import keyword
print(keyword.kwlist)


"""
# *********************  语法与句法2 ************************

* 赋值操作符： =  [注意： 不同于C语言，python的赋值语句不会返回值，如y=(x=1)将会报错]

    增量赋值：+=  -=  *=  /= //=   %=  **=  <<=  >>=  &=  ^=  |=  [注意: python不支持x++这样的前/后置的自增/减运算]
    
    链式赋值： x=1; y=x=x+1

    多重赋值： x=y=z=1

    多元赋值：(x,y,z) = (1,2,3)

* 内存管理： 变量无须事先声明，无须指定类型，赋值即可使用

    del语句： del obj1, obj2, ....., 或者 del(obj1, obj2, .....) [作用：删除对象的一个引用]
    id函数： id(obj) [作用：返加引用所指对象的内存地址]

* 对象

"""


"""
Reference:
[1]: https://blog.csdn.net/liang19890820/article/details/68488392
[2]: https://www.cnblogs.com/ECJTUACM-873284962/p/7576959.html
"""
