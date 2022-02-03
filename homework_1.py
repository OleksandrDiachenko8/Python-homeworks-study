#  PROGRAM1  
print('Введiть iм"я:')
name = input()
print('Введiть вiк:')
age = int(input())
while age < 0:
    print('Введений вiк некоректний, значення не може бути негативним!')
    print('Введiть правильний вiк:')
    age = int(input())
if age < 3:
    print(name + ' The Baby')
elif age < 16:
    print(name + ' The Child')      
else:
    print(name + ' The Adult') 
print('')  

#  PROGRAM2
for x in range(1,61):
        if x % 3 == 0:
            if x % 5 == 0:
                print('fizzbuzz')
            else:
                print('fizz')
        else:
            if x % 5 == 0:
                print('buzz')
            else:
                print(x)
print('')     

#  PROGRAM3
import random
print('Це гра вгадай число')
x = random.randint(1,10)
sproba = 0
print('Загадано число вiд 1 до 10. Вгадай його.')
while True:
    print('Спроба ',sproba+1,':')
    number=int(input())
    if number<x:
        print('Нi, це надто мало.')
    if number>x:
        print('Вибери число поменьше.')
    if number==x:
        print('Вiтаю, ти справився.')
        print('Тобi б в казино грати.')
        break
    sproba+= 1
print('')
