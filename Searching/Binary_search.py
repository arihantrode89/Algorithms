def Binary_search(A,s):
    l=0
    u=len(A)-1
    found=False
    while l<=u and not found:
        mid=int((l+u)/2)
        if s==A[mid]:
            found=True
        else:
            if s>A[mid]:
                l=mid+1
            else:
                u=mid-1
    return found
        
A=[i for i in range(1,1000)]
S_element=int(input())
print(Binary_search(A,S_element))
