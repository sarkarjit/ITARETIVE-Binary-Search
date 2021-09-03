def binSearch(mylist, l, h, key):
    f=-1
    while l<=h:
        mid = (l+h)//2
        if mylist[mid]<key:
            l=mid+1
        elif mylist[mid] > key:
            h=mid-1
        else:
            f=mid
            break

    return f


len=int(input("Enter the size of your list"))
mylist=[]
i=0
print("Please insert",len," elements in sorted order")
for i in range(len):
    n=int(input())
    mylist.append(n)

k = int(input("Enter your searching key"))

found = binSearch(mylist, 0, len-1, k)

if found==-1:
    print("Not found")
else:
    print("found at ", found+1, " position" )