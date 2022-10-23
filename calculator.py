def calc():
    sp = ['+', '-', '*', '/']
    try:
        a = input('Введите первое число:')
        a = int(a)
        while a != int(a):
            if a != int(a):
                print('Необходимо ввести первое число!!!')
                a = input('Введите первое число:')
        b = input('Enter: +,-,*,/')
        while b not in sp:
            if b not in sp:
                print('should be in: + or - or * or /')
                print('Enter +, -, *, /', '\n')
                b = input()
        c = input('Введите второе число:')
        c = int(c)
        while type(c) != int:
            print('Необходимо ввести второе число!!!')
            c = input('Введите второе число:')
            c = int(c)
            print(type(c))
        if b == '+':
            result = int(a + c)
            print('Результат: ', result)
        elif b == '-':
            result = int(a) - int(c)
            print('Результат: ', result)
        elif b == '*':
            result = int(a) * int(c)
            print('Результат: ', result)
        elif b == '/':
            result = int(a) / int(c)
            print('Результат: ', result)
    except ZeroDivisionError:
        result = 0
        print('На ноль делить нельзя')
    except ValueError:
        print('Необходимо ввести число')
calc()
