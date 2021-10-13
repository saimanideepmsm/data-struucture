#function defining bubble sort
def bubblesort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                a[j],a[j + 1]=a[j+1],a[j]
    return a
#driver code
l=list(map(int,input("enter the list of elements with space :").split()))
print(*bubblesort(l))