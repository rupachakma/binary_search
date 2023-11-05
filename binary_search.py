list=[1,2,3,4,5,6,7,9]
Search=3
found=0  
left,right=0,len(list)-1
while(left<=right):
    mid=(left+right)//2
    if list[mid]==Search:
        found=1
        break
    elif list[mid]<Search:
        left=mid+1
    else:
        right=mid+1
if found:
    print("found")
else:
    print("not found")

