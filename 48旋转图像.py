class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if not n:
            return
        data = []
        for l in range(n):
            for h in range(n-1, -1, -1):
                data.append(matrix[h][l])

        h_flag = 0
        l_flag = 0
        for num in data:
            matrix[h_flag][l_flag] = num
            l_flag += 1
            if l_flag > n - 1:
                h_flag += 1
                l_flag = 0

        return


matrix =[[1,2,3],[4,5,6],[7,8,9]]

Solution().rotate(matrix)

print(matrix)