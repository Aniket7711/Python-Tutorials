letter = '''
Dear <|name|>,
you are selected !
<|date|>'''
name = input("enter your name : ")
date = input("enter date: ")
print(letter.replace("<|name|>", name).replace("<|date|>", date))
# .rplace is used to replace the string in letter
