# 1
# def solution(number):
#     s = number
#     m = 0
#     if s >= 3:
#         for i in range(3,s):
#             if (i%3 == 0 or i%5 == 0):
#                 m=m+i
#     return m

# 2
# def duplicate_encode(word):
#     nn = []
#     word = word.lower()
#     for i in word:
#         if word.count(i) == 1:
#             nn.append('(')
#         else:
#             nn.append(')')
#     print(''.join(nn))

# 3
# def valid_braces(string):
#     brace = {'{':'}','(':')','[':']'}
#     stack = []
#     for i in string:
#         if i in '({[':
#             stack.append(i)
#         elif i in ')}]':
#             if len(stack) == 0 or brace[stack.pop()] != i:
#                 return False
#     return len(stack) == 0

# 4
def recoverSecret(triplets):
  string = list(set(i for t in triplets for i in t))
  for t in triplets * 2:
    fix(string, t[1], t[2])
    fix(string, t[0], t[1])
  return ''.join(string)


def fix(a, m, n):
  if a.index(m) > a.index(n):
    a.remove(m)
    a.insert(a.index(n), m)

# 5
  def disemvowel(string_):
    string = [i for t in string_ for i in t]
    for i in string_:
      if i.lower() in {'a', 'e', 'i', 'o', 'u'}:
        string.remove(i)
    string_ = ''.join(string)
    return string_


