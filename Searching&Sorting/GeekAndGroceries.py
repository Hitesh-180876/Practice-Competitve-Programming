# Hitesh Sharma
# 180876
# Lab Assignment 3
# Sorting & Searching

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
        
def PrintArr(ans, ans1):
    print(' '.join([i[0] for i in ans]))
    
        
t=int(input())
for _ in range(t):
    n,m,p,q=list(map(int,input().split()))
    first=[]
    second=[]
    for _ in range(n):
        i=input().split()
        first.append([i[0], int(i[1])])
    for _ in range(m):
        i=input().split()
        second.append([i[0], int(i[1])])
        
        
    mergeSort(first,0,n-1)
    mergeSort(second,0,m-1)
    ans=first[:p]+second[:q]
    ans1 = mergeSort(ans,0,p+q-1)
    PrintArr(ans, ans1)
