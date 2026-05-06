n = int(input())
marks = list(map(int, input().split()))
failed = False
for mark in marks:
	if mark < 40:
		failed = True
		break
if failed:
	print("Fail")
else:
	total = sum(marks)
	percentage = (total / n)
	print(f"Aggregate Percentage: {percentage:.2f}")

	if percentage > 75:
		print("Grade: Distinction")
	elif percentage >= 60:
		print("Grade: First Division")
	elif percentage >= 50:
		print("Grade: Second Division")
	elif percentage >= 40:
		print("Grade: Third Division")
