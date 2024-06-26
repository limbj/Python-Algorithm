import random
import time

randomlist = []
randomNumbers = random.choices(range(1,10000),k=100)    #1~10000사이 숫자중 랜덤하게 100개 뽑음
randomlist = randomNumbers


def compare_elements1(randomlist):      #알고리즘 A
    n = len(randomlist)
    for i in range(n-1):            #리스트의 i번째 항목과
        for j in range(i+1, n):     #i번째 다음의 리스트의 모든 항목 j 
            if randomlist[i] == randomlist[j]:  #i번째 항목과 j번째 항목이 같으면
                return True         #True
    return False                    #아니면 False


start1 = time.time()        #알고리즘 A 시간측정 시작

for i in range (10000):     #알고리즘 A 10000번 반복
    compare_elements1(randomlist)

end1 = time.time()          #알고리즘 A 시간측정 종료


randomlist.sort()                       #리스트 정렬(오름차순)

def compare_elements2(randomlist):      #알고리즘 B
    n = len(randomlist)
    for i in range(n-1):                        #리스트 i번째 항목이
        if randomlist[i] == randomlist[i+1]:    #그 다음 항목인 i+1번째 항목과 같으면
            return True                         #True
    return False                                #아니면 False


start2 = time.time()        #알고리즘 B 시간측정 시작

for i in range(10000):      #알고리즘 B 10000번 반복
    compare_elements2(randomlist)

end2 = time.time()          #알고리즘 B 시간측정 종료


print("알고리즘 A의 실행시간 = ",end1-start1)
print("알고리즘 B의 실행시간 = ",end2-start2)
