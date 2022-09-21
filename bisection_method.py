
import matplotlib.pyplot as plt
import numpy as np

#########################################
#
#       Alghorithm bisection method
#                                          
##########################################
def f(x):
    # return 10 - (np.power(x, 2.0) / 2.0) - (np.power(2.0, -x)) # 2 roots
    # return np.sin(2*x) - np.log(x)    # 1 root
    # return np.power(x, 3) - 6 * x + 2 # 3 roots
    # return 4 * np.cos(x) + 0.3 * x # 6 roots
    # return np.sqrt(1-x) - 5 * np.sin(2*x)
    return 2*np.power(x, 2.0) - 5 - np.power(2.0, x)
    

def divide_by_half(a, b, eps):
   
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        return 0, 0    
    cnt = 0
    while True:
        mid = (a + b) * 0.5
        if abs(b - a) < eps or abs( f(mid) ) < 0.0:
            return mid, cnt
       
        if (fa * f(mid) < 0.0):
            b = mid
            fb = f(mid)
        else:
            a = mid
            fa = f(mid)
        cnt += 1
########################################


count_sqrt = int(input('Введите колличество корней(целое число): '))
rangeof = int(input('Введите диапазон значений(целое число): '))
expanent = int(input('Введите точность(целое неотрицательное число): '))
mid_graph = rangeof // 2
range_sqrt = rangeof // count_sqrt

eps = np.exp(-expanent)

a = -rangeof
b = a + (range_sqrt)


plt.figure(figsize=(8, 5), dpi=80)
ax = plt.subplot(111)
x = np.linspace(-rangeof, rangeof)
y = (x - 2) * (x + 2)

s = f(x)
plt.plot(x, s)

print(len(s))

sq = []

i = 0
while a <= rangeof:
    
    a += range_sqrt
    b += range_sqrt
    
    # sq.append(divide_by_half(a, b, eps)[0])
    
    result = divide_by_half(a, b, eps)[0]
    
    if result == 0:
        continue
    
    sq.append(result)
    
    if i < count_sqrt:
        ax.plot(sq[i], 0, marker='s', color='blue')
        ax.vlines(sq[i], -y.max(), y.max(), color='r')
    else:
        break
        
    i += 1
    

print('Корни уравнения: ', sq[:len(s)])    

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([-rangeof, rangeof])
plt.ylim([-rangeof, rangeof])
plt.title('divide_by_half')
plt.grid(True)
plt.show()
