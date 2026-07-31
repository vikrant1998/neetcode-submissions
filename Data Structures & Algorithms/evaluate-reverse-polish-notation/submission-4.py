class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        q = deque()
        operatorSet = set()
        operatorSet.add('+')
        operatorSet.add('-')
        operatorSet.add('*')
        operatorSet.add('/')

        for token in tokens:
            if token in operatorSet:
                element2 = q.pop()
                element1 = q.pop()
                if token == '+': q.append(element1 + element2)
                elif token == '-': q.append(element1 - element2)
                elif token == '*': q.append(element1 * element2)
                elif token == '/': q.append(int(element1 / element2))
            else:
                q.append(int(token))

        return q.pop()