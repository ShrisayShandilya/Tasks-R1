class Solution(object):
    def generate(self, numRows):
        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        def C(n, k):
            return factorial(n)/(factorial(k) * factorial(n - k))

        
        triangle = []
        for n in range(numRows):
            row = []
            for k in range(n + 1):
                row.append(C(n, k))
            triangle.append(row)
        return triangle
