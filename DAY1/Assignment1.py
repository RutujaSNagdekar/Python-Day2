val = int(input("Enter Value in Inches"))
print("Select Option 1. Feet  2. Meters  3. Centimeters")
op = input("Enter your choice ")

if op=='Feet':
    feet = 12*val
    print("Inches to Feet", feet)
elif op=='Meters':
    meters = 39.37*val
    print("Inches to Meters", meters)
elif op=='Centimeters':
    cnt = 0.3937*val
    print("Inches to Meters", cnt)






