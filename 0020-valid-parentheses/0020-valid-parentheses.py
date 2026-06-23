class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        d = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1] != d[ch]:
                    return False
                stack.pop()

        return len(stack) == 0





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna