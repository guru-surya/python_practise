# PRIME NUMBERS

for num in range(100, 200):
    if all(num % i != 0 for i in range(2, num)):
        print(num)


 # SORT FUNCTIONS

l = [64,55,78,67,25,12,12,11,1,2,4]

l.sort(reverse=True)
print(l)


git add .
git commit -m "docs: add test comment"
git push origin feature/user-login

#  FIBONACCI SERIS

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

for i in range(1,10):
    print(f(i))

# REVERSE THE LIST

# numbers = [21, 1, 2, 3, 4, 9, 10, 15, 24]
#
#
# def reverse_list(lst):
#     return lst[::-1]
#
#
# print(reverse_list(numbers))

# PALINDROME OR NOT

# def is_palindrome(s):
#     rev = " ".join(reversed(s))
#
#     if s == rev:
#         return True
#     return False
#
# print(is_palindrome("hello world"))

# DUPLICATES IN A LIST

# l = [1,2,1,2,5,1,4,6,8]
# print(set([x for x in l if l.count(x) > 1]))


# JOIN TWO STRINGS

# test_string = "GFG"
# add_string = "is best"
# print(" the original string is: " + str(test_string))
# print(" the original string is: " + str(add_string))
#
# res= " ".join((test_string, add_string))
# print("the concatenated string is: " + res)

#





















