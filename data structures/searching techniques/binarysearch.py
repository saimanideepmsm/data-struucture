def binarysearch(arr,key):
    f=0           #front
    r=len(arr)-1  #rear
    while(f<=r):
        mid=(f+r)//2
        if key==arr[mid]:
            return mid
        if key<arr[mid]:
            r=mid-1
        if key>arr[mid]:
            f=mid+1
    return -1

#driver code
lst=list(map(int,input("enter the list of elements with a space bs: ").split()))
key=int(input("enter the key to search"))
c=binarysearch(lst,key)

print(c)