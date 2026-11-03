scores = [72, 45, 90, 61, 38]

passed = 0
total = 0

for score in scores:
    # 1. Grade calculation
    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    print(f'Score: {score}, Grade: {grade}')
    
    # 2. Pass count check
    if score >= 50:
        passed += 1
        
    # 3. Running total accumulator
    total += score

# Final summary calculations
failed = len(scores) - passed
average = round(total / len(scores), 1)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {average}")

# Bonus challenge outputs
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
