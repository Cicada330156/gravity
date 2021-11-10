bigG = (6.67408 * 10**(-11))

print("what is the distance between your masses")
radius = int(input())
print("what is your first object's mass?")
mass1 = int(input())
print("what is the second object's mass?")
mass2 = int(input())

fOfG = bigG * mass1 * mass2 / (radius**2)

print(f"force of gravity for masses {mass1} and {mass2} at distance {radius} is {fOfG} newtons.")
