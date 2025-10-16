# Pick one question from timed_challenge.txt #13
# Paste the question as a comment below
'''13. Balanced Symbols
Check if the brackets in a string are balanced.
Input: "{[()]}"
Output: True
Input: "{[(])}"
Output: False
'''
# Set a timer for 30 minutes and complete the question!
def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    tests = ["{[()]}", "{[(])}", "()", "(([]){})", "((())", "[{()}]"]
    for t in tests:
        print(f"{t} -> {is_balanced(t)}")


'''
this was really tough in 30 minutes for me to be honest. It really took me about 40, and I needed a little break
because I was honestly just stuck for a little, but i ended up figuring it out.
'''