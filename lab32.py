def detail(roll):
    x=[12,21,23,43,22,56,78]
    if roll in x:
        print("Roll number is Present",roll)
    else:
        print("Roll number is Absent",roll)
roll=int(input("Enter the roll number"))
detail(roll)