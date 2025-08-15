from functools import reduce

inp= (input("""Enter the list seprated by ",": """))

#converting input string to list
lst= list(map(float, inp.split(",")))

#sorting in decending order and copying first 3(or largest 3) in a new list
last3= sorted(lst, reverse=True)[0:3]

#Multiplying all three using reduce(imprt that from functool) and returning single value
result= reduce(lambda x, y: x * y, last3)

print(f"Your list = {lst}")
print(f"Largest 3 from your list: {last3}")
print("result: ", result)