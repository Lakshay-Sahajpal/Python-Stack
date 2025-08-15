def check_palindrome(x):
    #it will take ever item/word of the list and reverse it, if it is same as previous form, its a palindrome
    output = []
    output = (word for word in x if len(word) > 1 and word == word[::-1])
    '''output = []
    for word in x:
        if len(word)> 1 and word == word[::-1]:
            output.append(word)'''
    
    return output

#take list of string from user
#Hello madam this is a car which can race so it is a racecar 
list_str = input("Enter a string you want to check: ").lower()
list_in = list_str.split(" ")
print(list_in)

#call check_palindrome() 
result = check_palindrome(list_in)
print("Palindromes are: ", result)
