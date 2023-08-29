"""Calculator"""


def main():
    """start calculator"""

    print(f"******************************************************************\n"
          f"Добро пожаловать в самый простой калькулятор!\n"
          f"******************************************************************")
    num1 = float(input('Введите первое число > '))
    action = input('Выберите действие + - * / >')
    num2 = float(input('Введите второе число > '))

    if action == '+':
        result = num1 + num2

    elif action == '-':
        result = num1 - num2

    elif action == '*':
        result = num1 * num2

    elif action == '/':
        if num2 == 0:
            result = 'На ноль делить нельзя!'
        else:
            result = num1 / num2
    else:
        result = 'Нет такого действия!'
    print(f"###############################################\n"
          f"Результат Вашего выражения = {result}\n"
          f"###############################################\n")

    main()


if __name__ == '__main__':
    main()
