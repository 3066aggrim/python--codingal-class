import math

angle = float(input("Enter angle in degrees: "))

radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print("sin(", angle, ") =", sin_value)
print("cos(", angle, ") =", cos_value)
print("tan(", angle, ") =", tan_value)
