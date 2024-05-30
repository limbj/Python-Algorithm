def gcd(a,b):

    alist=[]

    for i in range(1, a+1):

        if a % i == 0:

            alist.append(i)

    for i in alist:

        for j in range(1, b+1):

            if b % j == 0:

                if i == j:

                    num1 = i    #a,b의 최대공약수 num1

    num2 = (a*b)//num1      #a,b의 최소 공배수는 a,b의 곱을 a,b의 최대공약수로 나눈값

    return num2

print("60과 28의 최소 공배수 =",gcd(60,28))
