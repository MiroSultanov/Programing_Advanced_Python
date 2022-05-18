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