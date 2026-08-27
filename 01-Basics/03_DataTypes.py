# 1. Integer

age = 20
marks = 95
temperature = -5

print(age)
print(marks)
print(temperature)
print(type(age))


# 2. Float

price = 99.99
height = 5.8
percentage = 87.5

print(price)
print(height)
print(percentage)
print(type(price))


# 3. Complex

z = 3 + 4j

print(z)
print(type(z))


# 4. Real and Imaginary Parts

z = 3 + 4j

print(z.real)
print(z.imag)


# 5. String

name = "Ashwani"

print(name)
print(type(name))


# 6. Single and Double Quotes

name1 = "Ashwani"
name2 = 'Ashwani'

print(name1)
print(name2)


# 7. Boolean

is_student = True
is_working = False

print(is_student)
print(is_working)
print(type(is_student))


# 8. Boolean from Comparison

a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)


# 9. None

result = None

print(result)
print(type(result))


# 10. Variable with None

answer = None

print(answer)

answer = 100

print(answer)


# 11. Checking Data Type

x = 100

print(type(x))

x = 10.5

print(type(x))

x = "Python"

print(type(x))

x = True

print(type(x))


# 12. isinstance()

age = 20

print(isinstance(age, int))
print(isinstance(age, str))


# 13. isinstance() with Multiple Types

x = 10.5

print(isinstance(x, (int, float)))


# 14. Dynamic Typing

x = 10

print(x)
print(type(x))

x = 10.5

print(x)
print(type(x))

x = "Python"

print(x)
print(type(x))


# 15. Object Identity

x = 100

print(id(x))