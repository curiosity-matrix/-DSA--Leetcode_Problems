class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
       
        last_index = {}

       
        for i in range(len(s)):
            last_index[s[i]] = i

        stack = []
        visited = set()

        for i in range(len(s)):
            ch = s[i]

            if ch in visited:
                continue

            while (stack and
                   ch < stack[-1] and
                   i < last_index[stack[-1]]):

                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna