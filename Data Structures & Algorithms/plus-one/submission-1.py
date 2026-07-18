class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        
        if digits[i] == 10:
            digits[i] = 0
            i -= 1
            carry = 1
            while i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += 1
                    carry = 0
                    break
                i -= 1
            if carry == 1:
                digits.insert(0, 1)
        return digits
        