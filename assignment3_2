str = "ADBAAEDBAB"

def count_substr1(str,A,B): #억지 기법 알고리즘
    count = 0
    n = len(str)
    for i in range(n-1):    #문자열 탐색
        if str[i] == A:     #문자열 중 A가 나오면
            for j in range(i+1, n): #그다음 문자열 탐색
                if str[j] == B:     #B가 나오면
                    count += 1      #+1
    return count

def count_substr2(str,A,B): #더 효율적인 알고리즘
    count = 0
    s = len(str)
    n = len(str)
    j = 0
    for i in range(n):  #문자열 탐색
        if str[i] == A: #A가 나오면
            count += 1  #+1
            s = i
        elif str[i] == B and s < i: #만약 B가 나오고 인덱스 값이 A값보다 뒤에 있을때
                j += count  #A가 나온횟수 더하기
    return j

count_substr1(str,"A","B")
print("방법 1 부분 문자열의 개수:",count_substr1(str,"A","B"))

count_substr2(str,"A","B")
print("방법 2 부분 문자열의 개수:",count_substr2(str,"A","B"))
