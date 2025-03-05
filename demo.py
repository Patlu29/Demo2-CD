name = input("Enter your name: ").upper()
age = int(input("Enter your age: "))
c_name = input("Enter company name: ").upper()

print(f"My name is {name} and my age is {age}. Now im working on {c_name}")
a = []
for i in range(1, 10):
    if i % 2 == 0: 
        a.append(i)
print(a)