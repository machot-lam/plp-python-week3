count = 1
total = 0

# BUG: Missing a colon (:) at the end of the while loop statement, which causes a SyntaxError. Added the colon.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Using a plus (+) operator to concatenate a string and an integer causes a TypeError. 
# Fixed by wrapping total in str() so Python can combine them, or by using an f-string.
print(f"Sum of 1 to 5 is: {total}")