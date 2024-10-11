import random
fruits = ['Apple','Orange','Mango']
for fruit in fruits :
    print(fruit)

student_score = [100,150,120,130,110,150,147,250,89,68,56,39,78]
sum = 0
for score in student_score :
    sum += score

print(sum)

print("Max score in betweeen the student is ",max(student_score))

max_score = 0
for score in student_score:
    if score > max_score :
        max_score = score
print(max_score)


sum = 1
for i in range(1,101,1):
    sum *= i

print(sum)

n1 = int(input("How many alphabets u want for the password"))
n2 = int(input("How many numbers u want for the password"))
n3 = int(input("How many special character u want for the password"))

letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","S","t","u","v","w","x","y","z"]
number = [1,2,3,4,5,6,7,8,9,0]
special_character = ["!","@","#","$","%","&","*"]

password = []
for i in range(0,n1):
    letters = random.choice(letter)
    password.append(letters)

for i in range(0,n2):
    numbers = random.choice(number)
    password.append(numbers)

for i in range(0,n3):
    special_character = random.choice(special_character)
    password.append(special_character)

print(password)

print(password)
print(random.shuffle(password))

print("Finale password is :",password)
