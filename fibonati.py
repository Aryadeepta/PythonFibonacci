def Fibo(n, a=1, b=1):
    return [a,b]+[(b:=a+(a:=b)) for i in range(n-2)]
print(Fibo(int(input("# of terms: ")),int(input("a: ")),int(input("b: ")))[-1])
