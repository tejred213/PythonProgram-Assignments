print("Enter the marks of three subjects::") #ass1 Q2

subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())

total, average, percentage, grade = None, None, None, None

total = subject_1 + subject_2 + subject_3 
average = total / 3.0
percentage = (total / 300.0) * 100

if average >= 90:
    grade = 'A'
elif average >= 80 and average < 90:
    grade = 'B'
elif average >= 70 and average < 80:
    grade = 'C'
elif average >= 60 and average < 70:
    grade = 'D'
else:
    grade = 'E'

print ("\nThe Total marks is:   \t", total, "/ 300.00")
print ("\nThe Average marks is: \t", average)
print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe Grade is:         \t", grade)