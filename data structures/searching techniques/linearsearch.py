def linearsearch(arr,key):
    for i in range(len(arr)):
        if key==arr[i]:
            return i
    return -1
#driver code
lst=list(map(int,input("enter the list of elements with a space ").split()))
key=int(input("enter the key to search"))
if linearsearch(lst,key):
    print("element found at",linearsearch(lst,key))
else:
    print("element isnt found")