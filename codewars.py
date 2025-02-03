text = "Banana and Mango"
num_a = text.count("a")
print(num_a)
# -------------

# Repeat strings (8 kyu)
def repeat_str(repeat, string):
    return repeat * string
# --------------

"""Complete the square sum function so that it squares each number passed into it and then sums the results together."""
def square_sum(numbers):
    return sum(x**2 for x in numbers)
# ------------

# Convert number to reversed array of digits (7 kyu)
"""Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
"""
# def digitize(n):
#     if n == 0:
#         return [0]
#     print [int(d) for d in str(n)[::-1]]
    
# digitize(52341)   
# -----------

# Highest and lowest (7 kyu)

# def high_and_low(numbers):
#     num_list = [int(x) for x in numbers.split()]
#     max_num = max(num_list)
#     min_num = min(num_list)
#     print(f"{str(max_num)} {str(min_num)}")

# high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
# -------------

# Square every digit (7 kyu)

# def square_digits(numbers):
#     print (int("".join(str((int(i))**2) for i in str(numbers))))
# ------------ 

# Descending order (7 kyu)
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
# def descending_order(num):
#     num_list = (sorted(list(str(num))))
#     num_str = str("".join(num_list))
#     print (int(num_str[::-1]))
# descending_order(34512)
# ------------

# Circumference of a circle
# ------------

# Area or Perimeter 
# def area_or_perimeter(l , w):
#     if l == w:
#         ans = w ** 2
#     else:
#         ans = 2*(l+w)
#     return(ans)
# area_or_perimeter(4,8)
# ------------
