def GetNumbers():  # Функция для получения чисел от пользователя
    numbers = []  # Создает пустой список для хранения чисел
    while True:  # Бесконечный цикл до ввода 'done'
        value = input("Enter a number (or 'done' to finish): ")  # Запрашивает ввод числа или 'done' для завершения
        if value.lower() == 'done':  # Если введено 'done'
            break  # Выход из цикла
        if value.isdigit() and int(value) > 0:  # Если это положительное число
            numbers.append(int(value))  # Добавляет число в список
        else:  # Иначе
            print("Invalid input, please enter a positive integer.")  # Выводит сообщение об ошибке
    return numbers  # Возвращает список чисел

def Factorial(n):  # Функция для вычисления факториала через рекурсию
    """
    Calculates the factorial of n using recursion.
    n must be a positive integer.
    Example: Factorial(5) returns 120 (5*4*3*2*1)
    """
    if n <= 0:  # Если n меньше или равно 0
        return "n must be a positive integer."  # Возвращает сообщение об ошибке
    elif n == 1:  # Если n равно 1
        return 1  # Возвращает 1 (базовый случай рекурсии)
    else:  # Иначе
        return n * Factorial(n - 1)  # Возвращает n умноженное на факториал (n-1)

def HelloWorldPrint():  # Функция для вывода приветствия
    print('Hello, World!')  # Печатает приветственное сообщение

def GetFactorial():  # Функция для получения и вычисления факториала от пользователя
    """Get factorial number from user and calculate it."""  # Получает факториал от пользователя и вычисляет его
    while True:  # Бесконечный цикл для ввода
        fact_input = input("Enter a number for factorial calculation (1-1000): ")  # Запрашивает число для факториала (1-1000)
        if fact_input.isdigit() and 1 <= int(fact_input) <= 1000:  # Если число в диапазоне 1-1000
            fact_number = int(fact_input)  # Преобразует строку в целое число
            result = Factorial(fact_number)  # Вычисляет факториал
            print(f"Factorial of {fact_number} is: {result}")  # Выводит результат
            break  # Выход из цикла
        else:  # Иначе
            print("Invalid input! Please enter a positive integer between 1 and 1000.")  # Выводит сообщение об ошибке
def 