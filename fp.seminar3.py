import random
#T(n) - number of steps the algorithm does
#O(n) - average; Thata(n) - worst case scenario;

#T(n)=10*n=O(n)
def f_1(n:int):
    for i in range(10): #10 steps
        for j in range(n): #n steps
            print("Hello World") #O(1)

#T(n)=10*n=O(n)
def f_2(n:int):
    for i in range(n, n+10): #10 steps
        for j in range(n): #n steps
            print("Hello World") #O(1)

#T(n)=(n-1)(n-1)=O(n^2)
def f_3(n:int):
    for i in range(1,n): #n-1 steps
        for j in range(i, n): # n-1, n-2, n-2, ..., 1 steps = n(n-1)/2 = O(n^2)
            print("kf") #O(1)

#T(n)=O(n^2)
def f_4(n: int):
    for i in range(n): #n-1 steps
        for j in range(2 * i + 1): #2*0+1 + 2*1+1 + 2*2+1 ... steps
            print("Hello World") #2(1+2+3+...+n-1) + n = (2n(n-1)/2) + n = n(n-1)+n = O(n^2)

#T(n) = 1+2+3+...+n^2-1 => n^2(n^2-1)/2
#T(n) = (n^4-n^2)/2
def f_5(n: int):
    for i in range(n ** 2): #n^2 steps
        for j in range(i): #1, 2, 3, ..., n^2-1 steps
            print("Hello World")


#T(n)=n*log2(n)=O(n*log(n))
def f_6(n: int):
    for i in range(n):  # n steps
        t = 1
        while t < n: #log2(n)
            print("Hello World")
            t *= 2


#O(n+m)
def f_7(n, m: int):
    for i in range(0, n):  # n steps
        print("Hello World")
    for j in range(0, m):  # m steps
        print("Hello World")

#O(n)
def f_8(n, m: int):
    for i in range(0, n): #n steps
        print("Hello World")
    for j in range(0, n): #n steps
        print("Hello World")

#T(n) = n*2n = O(n^2)
def f_9(n: int):
    for i in range(n): # n steps
        for j in range(n): # n steps
            print("Hello World")
        for k in range(n):  # n steps
            print("Hello World")

#T(n) = n*(n+1)/2 = O(n^2)
def f_10(n: int):
    for i in range(n): #n steps
        for j in range(n, i, -1): #n+n-1...+1
            print("Hello World")

#T(n)=n+m=O(n+m)
#We consider complexity of random as O(1)
def f_11(n: int, m: int) -> None:
    a = 0
    b = 0
    for i in range(n): #n steps
        a = a + random()

    for i in range(m): #m steps
        b = b + random()

#T(n) = n/2*log2(n)=O(nlogn)
def f_12(n: int) -> None:
    k = 0
    for i in range(n // 2, n): #n//2 steps
        for j in range(2, n, pow(2, j)): #log2(n)
            k = k + n / 2

#n=len(data)

#T(n) = n*log3(n) = O(nlogn)
#S(n) = O(1)
def f_13(data: list) -> int:
    data_sum = 0
    for el in data: #n steps
        j = len(data)
        while j > 1: #log3(n) steps
            data_sum += el * j
            j = j // 3
    return data_sum

#T(n)=>1, n<=1
#    =>T(n/2)+T(n/2)+1, n>1 => 2^2*T(n/4)+2+1 = 2^3*T(n/8)+2^2+2+1=...=2^k*T(0/1)+2^(k-1)+..+2+1 = 2^k+2^(k-1)+..+2+1 = 2*2^k-1=2n-1 =>O(n)
#S(n)=O(log(n))
def f_14(data: list) -> int:
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_14(data[:m]) + f_14(data[m:])

data=[2, 3, 4, 5, 6, 7]
data1=data[:3]
data2=data[3:]

print(data1)
print(data2)
print(id(data1))
print(id(data2))


#T(n) = O(n^2*log(n^2))
#S(n)=O(1)
def f_15(n: int) -> int:
    s = 0
    for i in range(1, n ** 2): #n**2-1 steps
        j = i
        while j != 0: #log10(n^2)
            s = s + j - 10 * j // 10
            j //= 10
    return s

#T(n) => 1, n<=1
#     => 4*T(n/2)+1, n>1 => 4^2*T(n/4)+4+1 = 4^3*T(n/8) + 16 + 4 + 1 = 4^k + 4^(k-1)+...+4+1=4^(k+1)-1=4*4^k-1=4*n^2-1=O(n^2)
#S(n) = log2(n) = O(log(n))
def f_16(n, i: int) -> None:
    if n > 1:
        i *= 2
        m = n // 2
        f_16(m, i - 2)
        f_16(m, i - 1)
        f_16(m, i + 2)
        f_16(m, i + 1)
    else:
        print(i)

"""
Analyze the algorithm's time complexity. Write an equivalent algorithm with 
a strictly better time complexity
"""

#T(n)=O(n^2)
#S(n)=O(1)
def f_17(data: list) -> int:
    i = 0
    j = 0
    m = 0
    c = 0
    while i < len(data): # n steps
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data): # n steps maximum
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m

#T(n)=O(n)
#S(n) = O(n)
def betterTn_f17(data: list) -> int:
    dict_counter: dict = {}
    for num in data:
        dict_counter[num] = 0
    for num in data:
        dict_counter[num] += 1
    maximum = -1
    for num in data:
        maximum = max(maximum, dict_counter[num])
    return maximum
