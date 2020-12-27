def fibo(a,b,n):
    p=(1+5**.5)*.5
    q=(1-5**.5)*.5
    x=(b-q*a)/(p-q)
    y=(b-p*a)/(q-p)
    return(int(x*p**(n-1)+y*q**(n-1)))
print(fibo(int(input("First term: ")),int(input("Second term: ")),int(input("What term: "))))
