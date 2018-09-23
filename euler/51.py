import mathExt as M
import sys
import math


for length in range(3, 5): #sys.maxsize): # 숫자의 길이
    for x_length in range(1, length): # x의 개수 (1 ~ length-1) , 마지막 숫자는 1,3,7,9 로 정해져 있음
        num_length = length - x_length - 1
        num_start = int(math.pow(10, num_length-1)) if num_length > 0 else None
        num_end = int(math.pow(10, num_length)) if num_length > 0 else None

        position_list = []
        for i in range(x_length):
            element = []
            for x_pos in range(length - 1):
                element.append(x_pos)
            position_list.append(element)

        print(length, num_length,x_length, num_start, num_end, position_list)

        # x 위치 정하기
        # length = 4
        # x_length = 1
        # 0, 1, 2
        # x_length = 2
        # (0,1), (0,2), (1,2)

        # length = 5
        # x_length = 3
        # (0,1,2) (0,1,3) (0,2,3) (1,2,3)
        # x_length = 2
        # (0,1) (0,2) (0,3) (

        #for i in range(math.pow(10, num_length-1), math.pow(10, num_length-2)):
        #for last_num in [1, 3, 7, 9]: