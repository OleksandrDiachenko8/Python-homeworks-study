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

class Rectangle():
    def __init__(self, side_a, side_b):
        self.a = side_a
        self.b = side_b
        
    def perimeter(self):
        p = 2 * self.a + 2 * self.b
        print('Периметр прямокутника = ', end='')
        return (p)
    
    def square(self):
        s = self.a * self.b
        print('Площа прямокутника = ', end='')
        return (s)

class Triangle():
    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c
        
    def isExists(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) \
            and (self.b + self.c > self.a):
            print("Трикутник iснує")
            return True
        else:
            return False
        
    def perimeter(self):
        p = self.a + self.b + self.c
        print('Периметр трикутника = ', end='')
        return (p)
    
    def square(self):
        p = (self.a + self.b + self.c) / 2   
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)
        s ="{0:.4f}".format(s)
        print('Площа трикутника = ', end='')
        return (s)   

class Circle():
    pi = 3.14159
    def __init__(self, radius):
        self.r = radius
                
    def perimeter(self):
        p = 2 * self.pi * self.r
        p ="{0:.3f}".format(p)
        print('Периметр кола = ', end='')
        return (p)
    
    def square(self):
        s = self.pi * (self.r ** 2)
        s ="{0:.3f}".format(s)
        print('Площа кола = ', end='')
        return (s)



print('\nВiтаю, з якою фiгурою хочете працювати?')
print('1. Прямокутник', '2. Трикутник', '3. Коло', sep='\n')
figure_type = int(entryDataValidation(input(), [1,2,3]))

print('\nГарний вибiр, а що потрiбно обчислити?')
print('1. Периметр', '2. Площу', sep='\n')
property = int(entryDataValidation(input(), [1,2]))

if figure_type == 3:
    print('Введiть радiус:')
    circle = Circle(float(entryDataValidation(input())))
    if property == 1:
        res = circle.perimeter()
    else:
        res = circle.square()
else:
    print('Введiть сторони:')
    if figure_type == 2:
        a = float(entryDataValidation(input()))
        b = float(entryDataValidation(input()))
        c = float(entryDataValidation(input()))
        triangle = Triangle(a, b, c)
        if triangle.isExists():
            if property == 1:
                res = triangle.perimeter()
            else:
                res = triangle.square()
        else:
            res = 'Такий трикутник не iснує!!!!!'
    else:
        a = float(entryDataValidation(input()))
        b = float(entryDataValidation(input()))
        rectangle = Rectangle(a, b)
        if property == 1:
            res = rectangle.perimeter()
        else:
            res = rectangle.square()
print(res)

print(type(Circle))


