class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: return s
        
        idx = 0
        step = 1
        rows = [''] * numRows

        for char in s:
            rows[idx] += char
            if idx == numRows - 1:
                step = -1
            elif idx == 0:
                step = 1
            idx += step

        return ''.join(rows)