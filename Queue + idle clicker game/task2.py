import math
from matplotlib import pyplot as plt

if __name__ == "__main__":
    nList = [1 << i for i in range(8)]   # creating the list

    O1 = [1 for n in nList]     # doing the mathematical operations
    Ologn = [math.log2(n) for n in nList]
    On = [n for n in nList]
    Onlogn = [n*math.log2(n) for n in nList]
    On2 = [pow(n, 2) for n in nList]
    O2n = [pow(2, n) for n in nList]

    plt.plot(nList, O1, label='O(1)', linewidth=1)  # plotting the results
    plt.plot(nList, Ologn, label='O(logn)', linewidth=1)
    plt.plot(nList, On, label='O(n)', linewidth=1)
    plt.plot(nList, Onlogn, label='O(nlogn)', linewidth=1)
    plt.plot(nList, On2, label='O(n2)', linewidth=1)
    plt.plot(nList, O2n, label='O(2^n)', linewidth=1)

    plt.title('Complexity Plots')
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.legend()
    plt.show()
