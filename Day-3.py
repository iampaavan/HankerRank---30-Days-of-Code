number = int(input('Enter a number: '))

if number % 2 != 0:
    print(f"Weird")

else:
    if 2 <= number <= 5:
        print(f"Not Weird")
    elif 6 <= number <= 20:
        print(f"Weird")
    else:
        print(f"Not Weird")