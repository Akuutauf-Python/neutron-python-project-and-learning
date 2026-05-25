# operator logika
v = 3
x = 10
y = 3

# and = true (true && true)
z = v <= y and y < x
print(z)

# or = true (false || true)
z = x < v or y < x
print(z)
