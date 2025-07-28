def primos (n):
    primos = []
    num = 2 #El primer número primo
    
    while len(primos) < n:
        es_primo = True
        for p in primos:
            if p * p > num:
                break
            if num % p == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
        num+=1
    return primos
