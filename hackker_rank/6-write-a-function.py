def is_leap(year_parameter):
    leap = False

    # Write your logic here
    if year_parameter % 4 == 0:
        leap = True
    if year_parameter % 100 == 0:
        leap = False
    if year_parameter % 400 == 0:
        leap = True
    return leap


year = int(input())
print(is_leap(year))
