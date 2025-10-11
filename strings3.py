# let X rep a string; T be a target character to search
# let I represent index of string
# while i < len(X), if X[1] == T then reutrn i else i+1
# if T is not found, return -1

# first argument function ~~~
def str_search(text, target):
    if not text: #truthy falsy ; len(text) == 0
        return -1
    else:
        i = 0
        while i < len(text):
            if text[i] == target:
                return i # the locaiton of target
            i += 1
        # end of while
        return -1

print("Jasper...where is p?", str_search("Jasper", "p"))
    

