def gcd(a,b):

    alist=[]        #alist 생성 

    blist=[]        #blist 생성

    for i in range(1, a+1):

        if a % i == 0:      #a의 약수

            alist.append(i) #a의 약수 alist에 저장

    for i in range(1, b+1):

        if b % i == 0:      #b의 약수

            blist.append(i) #b의약수 blist에 저장

    for i in alist:

        for j in blist:

            if i == j:      #a의 약수와 b의 약수가 같으면

                a = i       #a의 약수로 초기화

    return a

print("60과 28의 최대 공약수 =",gcd(60,28))
