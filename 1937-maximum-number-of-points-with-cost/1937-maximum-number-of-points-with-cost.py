class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev = points[0][:]

        for r in range(1, m):
            left = [0] * n
            right = [0] * n

            # Left-to-right pass: carry best value from the left with -1 penalty
            left[0] = prev[0]
            for j in range(1, n):
                left[j] = max(prev[j], left[j - 1] - 1)

            # Right-to-left pass: carry best value from the right with -1 penalty
            right[-1] = prev[-1]
            for j in range(n - 2, -1, -1):
                right[j] = max(prev[j], right[j + 1] - 1)

            # Transition: combine current points with the best available column from above
            curr_row = [0] * n
            for j in range(n):
                curr_row[j] = points[r][j] + max(left[j], right[j])

            prev = curr_row

        return max(prev)