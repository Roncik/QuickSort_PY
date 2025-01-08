import math
import time
import random
import sys

def partition(A, p, r):
    x=A[r]
    i=p-1
    for j in range(p, r+1):
        if A[j]<=x:
            i=i+1
            A[i], A[j] = A[j], A[i]
    if i<r:
        return i
    else:
        return i-1
    
def QuickSort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        QuickSort(A,p,q)
        QuickSort(A,q+1,r)
        
def QuickSortModified(A, p, r, c):
    if p + c < r:  
        q = partition(A, p, r)
        QuickSortModified(A, p, q, c)
        QuickSortModified(A, q + 1, r, c)

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def HybridQuickSort(A, c):
    QuickSortModified(A, 0, len(A) - 1, c)  
    insertion_sort(A)  

def TestQuickSort(A, rand):
    n=1000
    while n<4000:
        A = []
        if (rand == True):
            for i in range(n):
                A.append(random.randint(1,500))
        else:
            x = n
            for i in range(n):
                A.append(x)
                x-=1
        start = time.time()
        QuickSort(A,0,len(A)-1)
        end = time.time()
        elapsed = end-start
        print('Size: ', n, ' Execution time:', elapsed, 'seconds')
        n+=100
        
def TestModifiedQuickSort(A, rand):
    n=1000
    while n<4000:
        A = []
        if (rand == True):
            for i in range(n):
                A.append(random.randint(1,500))
        else:
            x = n
            for i in range(n):
                A.append(x)
                x-=1
        start = time.time()
        HybridQuickSort(A,c=4)
        end = time.time()
        elapsed = end-start
        print('Size: ', n, ' C: ', 4, ' Execution time:', elapsed, 'seconds')
        n+=100
    

sys.setrecursionlimit(1000000)

Tablica = []

TestModifiedQuickSort(Tablica, False)


# n=10000
# for i in range(n):
#     Tablica.append(random.randint(1,500))
    
# HybridQuickSort(Tablica, 3)
# print(Tablica)


    
    

