# 学习笔记

## 异常处理

- 异常捕获使用try...except语法

- 常见的异常类型

    - LookupError下的IndexError、KeyError

    - IOError

    - NameError

    - TypeError

    - AttributeError

    - ZeroDivisionError

- 也可以自定义异常类型

- finally: 无论异常是否处理都会执行的语句

## 数据库操作（mysql）

- 使用PyMySql包进行数据库操作

    1. 定义host、port、user、password、db等基本信息

    2. 使用pymysql的connect方法连接数据库

    3. 使用cursor开启游标

    4. 使用execute方法执行sql语句
        - 用try...except包裹处理可能出现的异常

    5. 完成后关闭游标，断开数据库连接

## 反爬虫

- 模拟浏览器的头部信息

- 加入cookies验证信息

- 使用webDriver模拟浏览器行为

    - webDriver模拟登录行为

        1. 使用webdriver调起浏览器，访问目标地址

        2. 使用find_element_by_xpath找到输入框input标签，send_keys
        传入用户名和密码，找到登录的a标签或button按钮，用click方法模拟点击

        3. get_cookies方法获取登录后的cookies

        3. 处理异常，关闭浏览器

- 代理IP

    - 在中间件middlewares中自定义继承自HttpProxyMiddleware的类，在setting中设置获建立动态的代理IP池传入代理IP并处理成标志格式随机抽取使用

- 分布式爬虫

    - redis