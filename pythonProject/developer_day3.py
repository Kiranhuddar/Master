# print("Welcome to my park")
# height = int(input("Enter your height"))
# if height >=150:
#     print("your eligible for riding")
# else:
#     print("yout not elegilble for riding")

# amount = 0
# print("Welcome to python pizza deliveries")
# size = input("What size pizza do you want ? S or M or L")
# if size =="s":
#     amount+= 10
# elif size=="m":
#     amount+=15
# else:
#     amount+=20
# print("Total amount to be paid is ",amount)
# age = 56
# if 45 >= age and age <55:
#     print("ndsankdja")

print('''
         ,,,,,,,,
           ,|||````||||
     ,,,,|||||       ||,
  ,||||```````       `||
,|||`                 |||,
||`     ....,          `|||
||     ::::::::          |||,
||     :::::::'     ||    ``|||,
||,     :::::'               `|||
`||,                           |||
 `|||,       ||          ||    ,||
   `||                        |||`
    ||                   ,,,||||
    ||              ,||||||```
   ,||         ,,|||||`
  ,||`   ||   |||`
 |||`         ||
,||           ||
||`           ||
|||,         |||
 `|||,,    ,|||
   ``||||||||`fr
''')

print('''
|\    \ \ \ \ \ \ \      __   
|  \    \ \ \ \ \ \ \   | O~-_
|   >----|-|-|-|-|-|-|--|  __/
|  /    / / / / / / /   |__\  
|/     / / / / / / /
''')

print("welcome to the treasure land")

ask_direction = input("where do u want to go ? left or right").lower()
if ask_direction == "left":
    print("Oops game over for you")
elif ask_direction == "right":
    next_level = input("what u wan to do ? swim or wait").lower()
    if next_level == 'swim':
        print("sorry better luck next time")
    elif next_level == "wait":
        print("COngrats you passs second level")
        door = input("which door u want to go ? red or blue").lower()
        if door == "red":
            print("oops game over")
        elif door == "blue":
            print("oops game over")
        elif door == "yellow":
            print("congratulkation "
                  "u won")
        else:
            print("enter correct door")

