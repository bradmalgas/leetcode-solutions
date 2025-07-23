class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)-1):
            curr = s[i]
            after = s[i+1]

            if curr == 'I' and (after == 'V' or after == 'X'):
                total -= convert.get(curr)
            elif curr == 'X' and (after == 'L' or after == 'C'):
                total -= convert.get(curr)
            elif curr == 'C' and (after == 'D' or after == 'M'):
                total -= convert.get(curr)
            else:
                total += convert.get(curr)
        total += convert.get(s[-1])
        return total
