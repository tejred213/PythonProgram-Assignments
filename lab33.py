def detail(roll):
    x=[21,54,23,22,56]
    if roll in x:
        print(f"Roll number {roll} is present")
    else:
        print(f"Roll number {roll} is absent")
roll = int(input("enter roll no"))#24
detail(roll)