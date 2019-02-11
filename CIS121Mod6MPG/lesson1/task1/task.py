# author:
# date:
# purpose: Miles Per Gallon

# input
isErrorGallon = True
isErrorMile = True

while isErrorMile:
    try:
        miles = float(input("Plesse enter miles driven: "))
        if miles >= 0:
            isErrorMile = False
    except:
        isErrorMile = True

while isErrorMile:
    try:
        gallons = float(input("Plesse enter gallons used: "))
        if gallons >= 0:
            isErrorGallon = False
    except:
        isErrorMile = True


# calculation
MPG = miles / gallons


# output
print("Miles =", miles, "\nGallons =", gallons, "\nMiles Per Gallon=", MPG)
