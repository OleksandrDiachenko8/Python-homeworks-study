def entryDataValidation (entry_data, data_possible=[]):
    while True:
        if len(data_possible) > 0:            # Якщо вказаний другий аргумент
            if entry_data.isdigit() and (float(entry_data) in data_possible):
                break
            else:
                print(f'Введiть коректне значення (цiле вiд {data_possible[0]} до {data_possible[len(data_possible) - 1]}):')
                entry_data = input()
        else:
            if entry_data.replace('.','',1).isdigit() and float(entry_data) > 0:
                return entry_data
            else:
                print('Введiть коректне значення (позитивне число):')
                entry_data = input()
    return entry_data
                
def isTriangleExists(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Трикутник iснує")
        return True
    else:
        return False
            
def triangle(a, b, c, i):
    if i == 1:      # обчислити периметр
        p = a + b + c
        return ('Периметр трикутника = ' + str(p))
    else:           # обчислити площу
        p = (a + b + c) / 2   
        s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)  
    return ('Площа трикутника = ' + str(s))

def rectangle(a, b, i):
    if i == 1:
        p = 2 * a + 2 * b
        return ('Периметр прямокутника = ' + str(p))
    else:
        s = a * b
        return ('Площа прямокутника = ' + str(s))        

def circle(r, i):
    pi = 3.14159
    if i == 1:           # обчислити периметр
        p = 2 * pi * r
        return ('Периметр кола = ' + str(p))
    else:                # обчислити площу
        s = pi * (r ** 2)
        return ('Площа кола = ' + str(s))

print('\nВiтаю, з якою фiгурою хочете працювати?')
print('1. Прямокутник', '2. Трикутник', '3. Круг', sep='\n')
figure_type = int(entryDataValidation(input(), [1,2,3]))
print('\nГарний вибiр, а що потрiбно обчислити?')
print('1. Периметр', '2. Площу', sep='\n')
property = int(entryDataValidation(input(), [1,2]))
if figure_type == 3:
     print('Введiть радiус:')
     radius = float(entryDataValidation(input()))
     res = circle(radius, property)
else:
    print('Введiть сторони:')
    if figure_type == 2:
        a = float(entryDataValidation(input()))
        b = float(entryDataValidation(input()))
        c = float(entryDataValidation(input()))
        exists = isTriangleExists(a, b, c)
        if exists:
            res = triangle(a, b, c, property)
        else:
            res = 'Такий трикутник не iснує!!!!!'
    else:
        a = float(entryDataValidation(input()))
        b = float(entryDataValidation(input()))
        res = rectangle(a, b, property)
print(res)