#선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]: #선형 탐색을 시행
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
'''
선택 정렬은 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다. 
예를 들어 맨 앞 7과 0이 바뀌어 0이 맨앞에 온다면 0은 정렬이 된(처리가 된)데이터 이다.
시간 복잡도는 O(N^2)
'''

#삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
'''
처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다. 선택 정렬에 비해 구현 난이도가 높지만, 일반적으로 더 효율적이게 동작한다. 
오름차순을 가정으로 정렬하고 있으니, 왼쪽을 기준으로 비교하여 자신의 자리를 찾아간다. 
삽입 정렬의 시간 복잡도는 O(N^2)이다. 삽입 정렬은 현재 리스트의 데이터가 정렬되어 있는 상태라면 매우 빠르게 동작한다. 
최선의 경우 O(N)의 시간 복잡도를 가지게 된다. 
'''
#퀵 정렬(파이썬 장점을 살린)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
'''
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다. 
병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다. 

퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가진다. 
하지만 최악의 경우 O(N^2)의 시간 복잡도를 가진다. 

다양한 프로그래밍 언어에서 표준 정렬 라이브러리를 제공할때 퀵 정렬 기반 라이브러리가 작성되었다면, NlogN이 나올 수 있도록 조정 해줘야 한다. 

참고로, 표준 라이브러리 이용한다면 기본적으로 NlogN을 보장하게 된다. 
'''
#계수 정렬

array = [5,8,3,7,9,1,1,0,2,5,6,7,8,9,4,6]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 

for i in range(len(count)): 
    for j in range(count[i]):
        print(i, end=' ')



#이코테 https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=4 을 통해 공부하였습니다.





