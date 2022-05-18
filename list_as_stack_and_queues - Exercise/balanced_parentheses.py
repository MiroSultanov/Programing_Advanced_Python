# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced. A sequence of parentheses is balanced
# if every opening parenthesis has a corresponding closing parenthesis that occurs after the former. There will be no interval symbols between the parentheses. 
# You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.


expression = input()
opening_brackets = []
balanced = True
pairs = {
    '(': ')',
    '[': ']',
    '{': "}"
}

for ch in expression:
    if ch in "([{":
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_brackets = opening_brackets.pop()
        if pairs[last_opening_brackets] != ch:
            balanced = False

    if not balanced:
        break
if not balanced or opening_brackets:
    print("NO")
else:
    print("YES")
