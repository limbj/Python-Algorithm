#import random

#print("N의 값을 입력하세요:", end=" ")
#N = int(input())
#arr = [0,1]*N
#random.shuffle(arr)

#arr1 = arr
#arr2 = arr
#arr3 = arr
#===============================
#질문할 부분


arr1 = [0,0,1,1,1,0,0,1,1,0,1,0]
arr2 = [0,0,1,1,1,0,0,1,1,0,1,0]
arr3 = [0,0,1,1,1,0,0,1,1,0,1,0]


def sort1(arr1):    #첫번째 방법
    print("시작:", arr1)
    s = 0               #리스트 변화 단계
    count = 0           #연산횟수
    n = len(arr1)
    for i in range(n):
        swapped = False             #리스트의 변화가 일어나지 않으면 False
        s += 1
        print("%d step:"%s, arr1)
        for j in range(n-1):
            count += 1
            if arr1[j] > arr1[j+1]:     #리스트의 j번째 항목보다 j+1의 항목이 작으면
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j] #두 항목 교환
                swapped = True
        if swapped == False:     #리스트의 변화가 일어나지 않으면 종료
            break

    print("연산 횟수:", count)
    print()

def sort2(arr2):    #두번째 방법
    print("시작:", arr2)
    s = 0               #리스트의 변화 단계
    count = 0           #연산횟수
    n = len(arr2)
    for i in range(n):
        s += 1
        print("%d step:"%s, arr2)
        swapped = False             #리스트의 변화가 일어나지 않으면 False
        for j in range(n-i-1):      #정렬이 완료된 마지막 항목은 제외함
            count += 1
            if arr2[j] > arr2[j+1]:     #리스트의 j번째 항목보다 j+1의 항목이 작으면
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j] #두 항목 교환
                swapped = True
        if swapped == False:    #리스트의 변화가 일어나지 않으면 종료
            break

    print("연산 횟수:", count)
    print()


def sort3(arr3):    #세번째 방법
    print("시작:", arr3)
    n = len(arr3)
    s = 0               #리스트의 변화 단계
    count = n           #연산횟수
    for i in range((n//2)): #리스트의 절반만 확인함
        swapped = False
        if arr3[i] == 1:    #항목 i가 1이면
            for j in range(n//2,n): #나머지 절반 확인
                if arr3[j] == 0:    #나머지 절반 항목 j중 0인 항목
                    arr3[i],arr3[j] = arr3[j],arr3[i]   #항목 i와 j교환
                    count += 1
                    s += 1
                    print("%d step:"%s, arr3)
                    swapped = True
            if swapped == False:    #리스트의 변화가 일어나지 않으면 종료
                break

    print("연산 횟수:", count)
    print()


sort1(arr1)
sort2(arr2)
sort3(arr3)
