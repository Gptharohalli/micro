def insertionsort(a):
    n=len(a)
    for i in range(1,n-1):
        v=a[i]
        j=i-1
        while j>=0 and a[j]>v:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=v
x=[34,46,43,40,52,50,68,70]
print("before sorting:",x)
insertionsort(x)
print("after sorting:",x)
