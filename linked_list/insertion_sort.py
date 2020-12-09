# 링크드리스트를 이용한 삽입 정렬
# 자료 배열의 모든 원소들을 앞에서부터 차례대로 이미 정렬된 부분과 비교하여
# 자신의 위치를 찾아냄으로써 정렬을 완성
"""
삽입정렬의 개념

1. 정렬할 자료를 두 개의 부분집합 S와 U로 가정
- 부분집합 S: 정렬된 앞부분의 원소들
- 부분집합 U: 아직 정렬되지 않은 나머지 원소들

2. 정렬되지 않은 부분집합 U의 원소를 하나씩 꺼내서 
   이미 정렬되어있는 부분집합 S의 마지막 원소부터 비교하면서 위치를 찾아 삽입

3. 삽입 정렬을 반복하면서 부분집합 S의 원소는 하나씩 늘리고,
   부분집합 U의 원소는 하나씩 감소하게 함

4. 부분집합 U가 공집합이되면, 삽입정렬이 완성된다.

>> 각 부분집합의 원소를 매번 비교해야하므로 시간복잡도는 n ** 2이다.

삽입정렬의 과정
초기 상태: 첫번째 원소는 정렬된 부분 집합 S로 생각하고, 나머지 원소들은
정렬되지 않은 부분 집합 U로 생각한다.

"""


def insertion_sort(arr):
    for end in range(1, len(arr)):  # 첫번째 원소를 정렬되어있다고 가정, 정렬이 끝나면 범위를 넓혀 나감
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr


arr = [2, 1, 5, 4, 3]
print(insertion_sort(arr))