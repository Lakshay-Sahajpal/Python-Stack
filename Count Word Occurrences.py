inp = "hello hi hello world hello"

inp_list = inp.split(" ")
print(inp_list)

word_count = {}  

for val in inp_list:
    if val in word_count:
        word_count[val] += 1
    else:
        word_count[val] = 1

print(word_count)
