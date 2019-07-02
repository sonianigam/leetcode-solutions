import numpy as np
import math

class Solution:
    def output_zigzag(self, s: str, num_rows: int) -> str:
        diag_ratio = (num_rows-2)/(num_rows+(num_rows-2))
        num_cols = int(math.ceil(diag_ratio*(len(s)) + ((1-diag_ratio)*(len(s)))/num_rows))
        output_matrix = np.zeros((num_rows, num_cols))

        max_index = len(s)-1
        col = 0
        index = 0
        iteration = 0

        output_matrix[0][col] = index

        while index < max_index:
            if iteration % 2 == 0:
                for row in range(1, num_rows):
                    if index >= max_index:
                        break
                    index+=1
                    output_matrix[row][col] = index
            else:
                for i in range(1, num_rows):
                    if index >= max_index:
                        break
                    col+=1
                    index+=1
                    row = num_rows-1-i
                    output_matrix[row][col] = index

            iteration+=1

        result = s[int(output_matrix[0][0])]

        for i in range(num_rows):
            for j in range(len(output_matrix[0])):
                c = int(output_matrix[i][j])
                if c == 0:
                    pass
                else:
                    result+=s[c]
        return result
