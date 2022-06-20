"""
av = 10
x = int(input("Enter How Many Candies You Want : "))


i = 1
while i <= x:
    if i > av:
        print("Out of Stock")
        break
    print("Candy", i)
    i += 1





for i in range(1,21):
    if i % 3 == 0:
        continue
    else:
        print(i)






for i in range(1, 51):
    if i % 2 != 0:
        pass
    else:
        print(i)

"""

# Assignments
# 1. Print First 50 Fibonacci Numbers

n1 = 0
n2 = 1
print(n1, n2 ,end=" ")
for i in range(1, 51):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end= " ")

print("\n\n")


# 2. Check a Given Number is Prime or Not

n = 11

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime Number")
    
