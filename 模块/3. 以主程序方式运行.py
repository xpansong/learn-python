import module_main
print(module_main.add(100,200)) #这里出现两个结果，一个是module_main模块中运算出来的30，一个是本模块中运算出来的300
'''如果不想要module_main模块中的结果怎么办？
在module_main模块中给print(add(a,b)加入一个前提条件，即只有
if __name__=__main__
print(add(a,b)
只有在点击运行module_main模块时才会运行print(add(a,b)运算，
换句话说，也就是module_main是主程序是才会运行'''