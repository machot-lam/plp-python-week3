scores = [72, 45, 90, 61, 38]
for score in scores :
    if score >= 80:
        Grade = "A"
    elif score >=70:
        Grade = "B"
    elif score >= 50:
        Grade = "C"
    else:
        Grade = "F"

    print(f"Scores:{score},Grade: {Grade}")

passed = 0

for score in scores:
    if score >= 50:
        passed += 1

print(f"Number of students passed: {passed}")
print(f"Number of students failed: {len(scores) - passed}")


scores = [72, 45, 90, 61,38]

total = 0

for score in scores:
    total += score

average = total / len(scores)

print("Total scores:", total)
print("Average score:", round(average, 1))

