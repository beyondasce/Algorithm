def hello(a :int): #经过简单的测试，发现int并不能用于检测类型
    print(a)

if __name__ == "__main__":
    hello(-1)
    hello("1a")
