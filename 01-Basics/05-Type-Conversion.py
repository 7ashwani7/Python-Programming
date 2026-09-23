# 1. int()

x = "100"

x = int(x)

print(x)
print(type(x))


# 2. float()

x = "10.5"

x = float(x)

print(x)
print(type(x))


# 3. str()

age = 20

age = str(age)

print(age)
print(type(age))


# 4. bool()

x = 10

print(bool(x))

x = 0

print(bool(x))


# 5. Boolean Conversion

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool(None))


# 6. Implicit Type Conversion

a = 10
b = 5.5

result = a + b

print(result)
print(type(result))


# 7. Explicit Type Conversion

a = 10
b = 5.5

result = a + int(b)

print(result)


# 8. String to Integer

age = input("Enter age: ")

age = int(age)

print(age)
print(type(age))


# 9. String to Float

price = input("Enter price: ")

price = float(price)

print(price)
print(type(price))


# 10. Multiple Integer Inputs

a, b = input("Enter two numbers: ").split()

a = int(a)
b = int(b)

print(a + b)


# 11. Multiple Inputs Using map()

a, b = map(int, input("Enter two numbers: ").split())

print(a + b)


# 12. Three Integer Inputs

a, b, c = map(int, input("Enter three numbers: ").split())

print(a + b + c)