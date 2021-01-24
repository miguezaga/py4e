letters = ['a', 'b', 'c']
letters2 = ['a', 'b', 'c']

def chop (t):
    t.pop(0)
    t.pop()
print(chop(letters))
print(letters)

def middle (t):
    new_t = t[1:-1]
    return new_t
print(middle(letters2))
print(letters2)
