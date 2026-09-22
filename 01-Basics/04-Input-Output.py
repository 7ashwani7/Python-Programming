# 1. Basic print()

print("Hello Python")
print("Welcome to Python")


# 2. Printing Numbers

print(10)
print(20)
print(10 + 20)
print(100 - 50)


# 3. Printing Multiple Values

name = "Ashwani"
age = 20

print(name, age)


# 4. sep Parameter

print("2026", "09", "22", sep="-")


# 5. sep with Multiple Values

print("C++", "Java", "Python", sep=" | ")


# 6. end Parameter

print("Hello")
print("Python")


# 7. Using end

print("Hello", end=" ")
print("Python")


# 8. Printing Without New Line

print("1", end=" ")
print("2", end=" ")
print("3", end=" ")
print("4")


# 9. Taking Input

name = input()

print(name)


# 10. Input with Message

name = input("Enter your name: ")

print(name)


# 11. Input Returns String

age = input("Enter your age: ")

print(age)
print(type(age))


# 12. Taking Two Inputs

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(first_name, last_name)


# 13. Multiple Inputs

a, b = input("Enter two values: ").split()

print(a)
print(b)


# 14. Three Inputs

a, b, c = input("Enter three values: ").split()

print(a)
print(b)
print(c)


# 15. Custom split Separator

a, b, c = input("Enter values: ").split(",")

print(a)
print(b)
print(c)


# 16. f-string

name = "Ashwani"
age = 20

print(f"My name is {name}.")
print(f"I am {age} years old.")


# 17. Multiple Variables with f-string

name = "Ashwani"
age = 20
branch = "CSE"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Branch: {branch}")


# 18. Expression in f-string

a = 10
b = 20

print(f"Sum = {a + b}")
print(f"Product = {a * b}")


# 19. sep and end Together

print("Python", "Java", "C++", sep=" | ", end=" -> ")
print("Programming Languages")