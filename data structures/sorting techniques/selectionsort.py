def s(arr):
    for i in range(len(arr)):
        mi=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[mi]:
                mi=j
        arr[mi],arr[i]=arr[i],arr[mi]
    print(*arr)

#driver code
l=list(map(int,input().split()))
s(l)