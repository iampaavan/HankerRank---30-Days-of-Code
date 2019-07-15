actual = input().split()
date_actual = int(actual[0])
month_actual = int(actual[1])
year_actual = int(actual[2])

expected = input().split()
date_expected = int(expected[0])
month_expected = int(expected[1])
year_expected = int(expected[2])

fine = 0

if year_actual > year_expected:
    fine = 10000

elif year_actual == year_expected:

    if month_actual > month_expected:
        fine = (month_actual - month_expected) * 500

    elif month_actual == month_expected and date_actual > date_expected:
        fine = (date_actual - date_expected) * 15

print(fine)
