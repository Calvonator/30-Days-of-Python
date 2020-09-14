from math import fsum
import fractions

# 1 Import the fractions module and create a Fraction from the float 2.25


frac = fractions.Fraction(2.25)
print(frac)



# 2 Import only the fsum function from the math module and use it to find the sum of the following series of floats:

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]

fracsum = fsum(numbers)

print(fracsum)









