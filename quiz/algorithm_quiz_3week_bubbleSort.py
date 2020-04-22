'''
    문제) 주어진 리스트를 오름차순으로 정렬하시오.
    
    list = [7,4,5,1,3]
    
    <1회전>
    0번 인덱스에 있는 7과 1번 인덱스에 있는 4를 비교하여 4가 더 작으므로 교환
    1번 인덱스에 있는 7과 2번 인덱스에 있는 5를 비교하여 5가 더 작으므로 교환
    2번 인덱스에 있는 7과 3번 인덱스에 있는 1을 비교하여 1이 더 작으므로 교환
    3번 인덱스에 있는 7과 4번 인덱스에 있는 3을 비교하여 3이 더 작으므로 교환
    
    결과
    list = [4,5,1,3,7]
    
    <2회전>
    0번 인덱스에 있는 4와 1번 인덱스에 있는 5를 비교하여 4가 더 작으므로 교환x
    1번 인덱스에 있는 5와 2번 인덱스에 있는 1을 비교하여 1이 더 작으므로 교환
    2번 인덱스에 있는 5와 3번 인덱스에 있는 3을 비교하여 3이 더 작으므로 교환
    
    결과
    list = [4,1,3,5,7]
    
    <3회전>
    0번 인덱스에 있는 4와 1번 인덱스에 있는 1를 비교하여 1이 더 작으므로 교환
    1번 인덱스에 있는 4와 2번 인덱스에 있는 3을 비교하여 3이 더 작으므로 교환
    
    결과
    list = [1,3,4,5,7]
    
    <4회전>
    0번 인덱스에 있는 1과 1번 인덱스에 있는 3을 비교하여 1이 더 작으므로 교환x
    
    결과
    list = [1,3,4,5,7]
    
    '''
list = [7,4,5,1,3]

def bubble_sort(list):
    for i in list:
        for j in list:
            if i < j : 
                i, j = j, i
            
    return list

print(bubble_sort(list))