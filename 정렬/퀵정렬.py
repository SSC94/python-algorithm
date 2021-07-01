arr = [5,9,1,3,4,2,7,6,8]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = len(arr) // 2
    arr_low, arr_pivot, arr_high = [], [], [] 
    for i in arr:
        if i < arr[pivot]: arr_low.append(i)
        elif i > arr[pivot]: arr_high.append(i)
        else: arr_pivot.append(i)
    return quick_sort(arr_low) + quick_sort(arr_pivot) + quick_sort(arr_high)
print(quick_sort(arr))
'''
    line7처럼 mutable 자료형을 다룰경우 같은 값이어도 각각 할당해주어야 한다. 
    만약 같이 할당할 경우 shallow copy가 되어서 다른 컨테이너의 값을 변경해도 
    값을 공유하는 모든 컨테이너의 값이 같이 변경된다.
'''
    
