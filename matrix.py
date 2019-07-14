from typing import List
import numpy as np
import pdb

class Solution:
    def update_matrix(self, matrix:List[List[int]]) -> List[List[int]]:
        num_rows = len(matrix)
        num_columns = len(matrix[0])
        zero_indices = []

        output = [[1 for i in range(num_columns)] for i in range(num_rows)]

        for x in range(num_rows):
            for y in range(num_columns):
                if matrix[x][y] == 0:
                    output[x][y] = 0
                    zero_indices.append((x,y))
        
        for x in range(num_rows):
            for y in range(num_columns):
                min_dist = 10000
                if output[x][y] == 0:
                    break

                for z in zero_indices:
                    if min_dist == 1: break

                    x_dist = abs(z[0] - x)
                    y_dist = abs(z[1] - y)
                    total_dist = x_dist + y_dist
                    
                    if total_dist < min_dist:
                        min_dist = total_dist

                output[x][y] = min_dist
        return output
