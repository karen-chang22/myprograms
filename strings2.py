# strings practice 2

#cleaning
def clean(text):
    #to return a string with everything lowercased
    #and without special characters nor numbers
    result = "" #empty container
    i = 0 #i for index # dont use 'index' bc its a funciton/method name
    while i < len(text): # cannot be equal to length, because index available is always lenght-1, else out of bounds
        if text[i].isalpha(): # checks if the character is a alphabet, returns True or False
            result = result + text[i].lower() #concatenation here
        i += 1
    #end while loop
    return result

# first algorithm leanred: Linear search
word = input("enter the text: ")
print(clean(word))