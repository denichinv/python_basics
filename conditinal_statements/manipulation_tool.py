string = input("Enter a string - ")

print("""
        1. Convert to uppercase
        2. Convert to lowercase
        3. Slice the string
        4. Calculate string length
        5. Loop through characters
        """)

options = int(input("Choose option from 1 to 5 - "))

if options == 1:
    print(string.upper())
elif options == 2:
    print(string.lower())
elif options == 3:
    print(string[slice(3,11)])
elif options == 4:
    print(len(string))
elif options == 5:
    for char in string:
        print(char)
else:
    print("Invalid choice!")