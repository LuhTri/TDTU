import numpy as np

def cau1():
    x = np.array([1, 3, 5, 2, 9])
    y = np.array([-1, 3, 15, 27, 29])

    print("len(x) =", len(x))
    print("len(y) =", len(y))

def cau2():
    n = 10

    #a
    b = np.arange(12, 12 + 2*n + 1)
    print("a.", b)

    #b
    c = np.arange(31, 31 + 2*n + 1)
    print("b.", c)

    #c
    x = np.arange(-n, n + 1)
    print("c.", x)

    #d
    y = np.arange(n, -n - 1)
    print("d.", y)

    #e
    z = np.arange(n - 2*8 - 1, n, 2)
    z = z[::-1]
    print("e.", z)
    
    #f
    w = [1/(2**i) for i in range(1, n + 1)]
    print("f.", w)

    #g
    def fibonacci(n):
        if n < 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    d = [1/fibonacci(i) for i in range(0, n)]
    print("g.", d)

    #k
    p = [i/(i + 1) for i in range(0, n + 1)]
    print("p.", p)

    #l
    o = [chr(i) for i in range(97, 123)]
    print("l.", o)

    #m
    s = [chr(i) for i in range(65, 91, 3)]
    print("m.", s)

def cau3(n):
    myList = np.logspace(1, n, n)
    print("Cau3:", myList)

x = [1, 2, 3]
y = [98, 12, 33]
def cau4(x, y):
    return x + y

def cau6():
    x = np.arange(0, 20, 2)
    print("a. First sixth elements of x: \n", x[0:6])
    print("b. Last fifth elements of x:\n", x[-5::])
    print("c. First, fourth and last elements of x:\n", x[[0, 3, -1]])
    print("d. First, third fifth and seventh elements of x:\n", x[[0, 2, 4, 8]])
    print("e. Elements with odd indices:\n", x[1::2])
    print("f. Elements with even indices:\n", x[0::2])

def cau7():
    x = np.array([3, 11, -9, -131, -1, 1, -11, 91, -6, 407, -12, -11, 12, 153, 371])
    #a
    print("a. MAX:", np.max(x))
    #b
    print("b. MIN:", np.min(x))
    #c
    print("c. INDEX of values of x > 10:")
    for i in range(0, len(x)):
        if (x[i] > 10):
            print(i, end='\t')
    print("\n")       

    #d
    print("d. Vecotr x in REVERSE order:\n", x[::-1])
    #e
    print("e. Vector x in ASCENDING order:\n", np.sort(x))
    #f
    print("f. Vector x in DESCENDING order:\n ", np.sort(x)[::-1])

    #g
    def cau7g(x):
        count = 0
        for i in range(0, len(x)):
            for j in range(i + 1, len(x)):
                if x[i] + x[j] == 0:
                    count += 1

        return count
    print("g. Count x[i] + x[j] == 0:", cau7g(x))

    #h
    def cau7h(x):
        count = 0
        for i in range(0, len(x) - 1):
            for j in range(i + 1, len(x)):
                if x[i] == x[j]:
                    count += 1

        return count
    print("h. Count total number of DUPLICATE elements:", cau7h(x))

    #i
    def cau7i(x):
        n = len(x)
        y = []
        for i in range(0, n):
            y.append(x[i] + x[n - i - 1])

        return y
    print("i. New vector y which y[i] = x[i] + x[n - i - 1]\n ", cau7i(x))

    #j
    def cau7j(n):
        def isArmstrongNumber(n):
            temp = n

            digits = 0
            list = []

            #Đếs n có bao nhiêu chữ số và thêm các chữ số có trong n vào trong list
            while (n > 0):
                digits += 1
                list.append(n % 10)
                n = (n - n % 10) / 10

            #Tính các tổng các chữ số có trong n lũy thừa với số chữ số
            sum = 0
            for i in list:
                sum += i**digits

            #Nếu tổng bằng số ban đầu thì return True và ngược lại
            return sum == temp

        #Kiểm tra các số trong x là số Armstrong thì thêm vào w
        w = []
        for i in x:
            if (isArmstrongNumber(i)):
                w.append(i)
        
        return w
    print("j. New vector w which contains ARMSTRONG number in x:\n", cau7j(x))

print("\n --- --- --- Cau 1 --- --- --- ---\n")
cau1()

print("\n --- --- --- Cau 2 --- --- --- ---\n")
cau2()

print("\n --- --- --- Cau 3 --- --- --- ---\n")
cau3(4)

print("\n --- --- --- Cau 4 --- --- --- ---\n")
print("Cau 4: Vector z = Vector x + Vector y:\n", cau4(x, y))

print("\n --- --- --- Cau 6 --- --- --- ---\n")
cau6()

print("\n --- --- --- Cau 7 --- --- --- ---\n")
cau7()


