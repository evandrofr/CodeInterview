class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row = "0"
        for i in range(n-1):
            new_row = ""
            for j in range(len(row)):
                if row[j] == "0":
                    new_row += "01"
                else:
                    new_row += "10"
            row = new_row
        return int(row[k-1])