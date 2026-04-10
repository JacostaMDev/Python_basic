# Taking miles input from user
miles = float(input("Enter value in miles: "))

# Conversion factor
conv_fact = 1.609344

# Calculate kilometers
kilometers = miles * conv_fact

# Print the results
print('%0.2f miles is equal to %0.2f kilometers' %(miles,kilometers))
