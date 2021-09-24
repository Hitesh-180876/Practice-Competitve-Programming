# Hitesh Sharma
# 180876

import sys

def merge(arr, l, m, r):
    i=0
    j=0
    index=l
    left=arr[l:m+1]
    right=arr[m+1:r+1]
    while i<len(left) and j<len(right):
        if left[i][1]<right[j][1]:
            arr[index]=left[i]
            i+=1
        elif left[i][1]>right[j][1]:
            arr[index]=right[j]
            j+=1
        else:
            if left[i][0]<right[j][0]:
                arr[index]=left[i]
                i+=1
            else:
                arr[index]=right[j]
                j+=1
        index+=1
        
    while i<len(left):
        arr[index]=left[i]
        index+=1
        i+=1
    while j<len(right):
        arr[index]=right[j]
        index+=1
        j+=1


def mergeSort(arr,l,r):
    if r-l>0:
        mid=(l+r)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)
        
        
T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N, M, P, Q = list(map(int, sys.stdin.readline().rstrip().split()))
    
    A = []
    for i in range(N):
        x = input().split()
        A.append([x[0], int(x[1])])
        
    B = []
    for i in range(N):
        x = input().split()
        B.append([x[0], int(x[1])])
        
    mergeSort(A,0,N-1)
    mergeSort(B,0,M-1)
    ans=A[:P]+B[:Q]
    mergeSort(ans,0,P+Q-1)
    print(' '.join([i[0] for i in ans]))
