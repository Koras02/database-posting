def binary_search(data, target):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        min_value = data[mid]
        
        if min_value == target:
            return mid # 찾을 시 인덱스 바로 반환
        elif target < min_value:
            high = mid - 1 # 찾을 값이 중간 값보다 작을 시 왼쪽 범위를 탐색
        else:
            low = mid + 1 # 찾을 값이 중간 값보다 크면 오른쪽 범위 탐색
    return -1 

# 이진 탐색 시 반드시 정렬된 리스트에서 사용
sort_list = [5,10,15, 25, 30,35] # 정렬 되지 않을 시 출력 X
target_value = 35

index = binary_search(sort_list, target_value)
if index != -1:
    print(f"탐색 결과: {target_value}는 {index}번째 인덱스에 있습니다")
else:
    print(f"탐색 결과: {target_value}는 검색 결과에 없습니다.")