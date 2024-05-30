def gcd(a,b):       #a가 b보다 작지 않아야 함

    print("gcd ({},{})".format(a,b))

    while b!= 0:    #b가 0이 아닐 때까지

        r = a%b

        a = b

        b = r

        print("gcd ({},{})".format(a,b))    #유클리드 알고리즘 과정 확인

    return a

print("60과 28의 최대 공약수 =",gcd(60,28))
