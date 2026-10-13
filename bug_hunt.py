count = 1
total = 0
# Bug: you must add a colon after the while statement. otherwise, it will throw a syntax error.
# Bug: incorrect loop condition. it should be count <= 5 instead of count < 5. otherwise, it will not include 5.
while count <= 5:
    
    total = total + count
    count = count + 1
# Bug: incorrect string concatenation. it should be str(total) instead of total.
print("Sum of 1 to 5 is: " + str(total))