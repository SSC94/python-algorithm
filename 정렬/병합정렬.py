arr = [5,9,1,3,4,2,7,6,8]

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    arr_low = merge_sort(arr[:mid])
    arr_high = merge_sort(arr[mid:])
    low = high = 0
    merged_arr = []
    while low < len(arr_low) and high < len(arr_high):
        if arr_low[low] < arr_high[high]:
            merged_arr.append(arr_low[low])
            low += 1
        else:
            merged_arr.append(arr_high[high])
            high += 1
    merged_arr+=arr_low[low:]
    merged_arr+=arr_high[high:]
    return merged_arr
print(merge_sort(arr))
    
