'''计算6*5*4*3*2*1的值'''
def fac(a):
    if a==1:
        return 1
    else:
        return a*fac(a-1)
print(fac(6))

'''计算从1加到100的值'''
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(100))