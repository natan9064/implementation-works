def insertion_sort(arr):
    initializations_count = 0
    comparisons_count = 0
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >-1 and arr[j]>key:
            comparisons_count +=1
            arr[j + 1] = arr [j]
            initializations_count+=1
            j = j-1 
        if j > -1:
            comparisons_count +=1

               
        arr[j + 1]=key    
        initializations_count+=1

    return initializations_count, comparisons_count          


a=[9,5,4,5,6,3,5,6,3,2,6,8]               
print(insertion_sort(a))   
