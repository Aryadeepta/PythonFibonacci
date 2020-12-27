def fibonatiAdjustable(a=1,b=1,n=2):    
    if(n==0):
        x = a
    if (n==1):
        x = b
    if(n>=2):
        x = fibonatiAdjustable(a,b,n-1)+fibonatiAdjustable(a,b,n-2)
    return(x)
f = input('First number: ')
s = input('Second number: ')
t = input('Term Number: ')
print(fibonatiAdjustable(int(f),int(s),int(t)))
