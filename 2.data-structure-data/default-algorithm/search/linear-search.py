my_list = [10, 22, 30, 45, 25]

def linear_search(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return i # 찾는 경우 인덱스를 반환
    return -1 # 찾지 못할 씨 -1

target_value = 22

index = linear_search(my_list, target_value)
if index != -1:
   print(f"탐색 결과: {target_value}는 인덱스 {index}번 쨰에 있습니다")
else:
   print(f"탐색 결과: {target_value}는 인덱스에 존재하지 않습니다.")