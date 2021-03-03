import random

def binary_search(sorted_data, target, low_index, high_index):
    if low_index > high_index:
        return False
    mid_index = (low_index + high_index)//2

    if target == sorted_data[mid_index]:
        return True
    elif target < sorted_data[mid_index]:
        return binary_search(sorted_data, target, low_index, mid_index-1)
    else:
        return binary_search(sorted_data, target, mid_index+1, high_index)
    



if __name__=='__main__':
    data = [random.randint(0,100) for i in range(10)]
    sorted_data = sorted(data)
    print(f"data : {data}")
    print(f"sorted data : {sorted_data}")
    start_point = 0
    data_len = len(data) - 1
    target = int(input('what number would you like to find?'))
    found = binary_search(sorted_data, target, start_point, data_len)

    print(found)