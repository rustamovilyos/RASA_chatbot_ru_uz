from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

# class Solution(object):
#     def isValid(self, s):
#         brackets = ['(', ')', '{', '}', '[', ']']
#         if s.startswith(('}', ')', ']')):
#             return False
#         elif s.count(brackets[0]) == s.count(brackets[1]):
#             return True
#         elif s.count(brackets[0]) != s.count(brackets[1]):
#             return False
#         elif s.count(brackets[2]) == s.count(brackets[3]):
#             return True
#         elif s.count(brackets[2]) != s.count(brackets[3]):
#             return False
#         elif s.count(brackets[4]) == s.count(brackets[5]):
#             return True
#         elif s.count(brackets[4]) == s.count(brackets[5]):
#             return True
#         else:
#             return False
#
#
# solution = Solution()
# print(solution.isValid('())'))
