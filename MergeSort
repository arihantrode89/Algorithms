def merge_sort(A):
    if len(A)>1:
        q=int(len(A)/2)
        Left=A[:q]
        right=A[q:]
        merge_sort(Left)
        merge_sort(right)
        i=j=k=0
        while i<len(Left) and j<len(right):
            if Left[i]<right[j]:
                A[k]=Left[i]
                i+=1
            else:
                A[k]=right[j]
                j+=1
            k+=1
        
        while i<len(Left):
            A[k]=Left[i]
            i+=1
            k+=1
        while j<len(right):
            A[k]=right[j]
            j+=1
            k+=1
    return A
A=[1,28,32,12,13]
sorted_list=merge_sort(A)
print(sorted_list)
