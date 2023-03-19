import random
import time
import sys

sys.setrecursionlimit(10**5)

randomlist = []
randomNumbers = random.choices(range(1,10000),k=1000)
randomlist = randomNumbers

def repeat_function(func, n):                       #함수 반복호출 함수
    if n == 0:
        return
    func
    repeat_function(func, n-1)

start1 = time.time()

def compare_elements1(randomlist):                  #알고리즘 A
    n = len(randomlist)
    for i in range(n-1):
        for j in range(i+1, n):
            if randomlist[i] == randomlist[j]:
                return True
    return False

repeat_function(compare_elements1(randomlist),2500)

end1 = time.time()

#print(randomlist)
print(compare_elements1(randomlist))
print(end1-start1)
print("")

randomlist.sort()                           #리스트 정렬

start2 = time.time()

def compare_elements2(randomlist):                  #알고리즘 B
    n = len(randomlist)
    for i in range(n-1):
        if randomlist[i] == randomlist[i+1]:
            return True
    return False

repeat_function(compare_elements2(randomlist),2500)

end2 = time.time()

#print(randomlist)
print(compare_elements2(randomlist))
print(end2-start2)