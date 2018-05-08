try:
    import math
    import tensorflow as tf
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("success!")
except ModuleNotFoundError:
    print("木有“Tensorflow”模块")
except ZeroDivisionError:
    print("错误：除数为零！")


try:
    a=7
    b=0
    print(a/b)
except:
    print("a除b错误")
    raise NameError("除数为零错误")
finally:
    print("不管怎样都会运行这里的代码")