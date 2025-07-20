def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)


show(5)

#returns n!

def fac(d):
    if(d == 0 or d == 1):
        return 1
    else:
        return d * fac(d-1)
    

ans = fac(4)

print(ans)
