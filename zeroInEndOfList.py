inp = [0, 0, 1, 2, 0, 5, 0, 0]

c = inp.count(0)

otp= [i for i in inp if i!=0]
        
for i in range (c):
    otp.append(0)

print(inp)
print(f"Your Output: {otp}")
        