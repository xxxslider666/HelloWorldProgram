import lib

def main():  # Главная функция программы
    lib.HelloWorldPrint()  # Вызывает функцию для вывода приветствия
    
    numbers = lib.GetNumbers()  # Получает список чисел от пользователя
    if numbers:  # Если список содержит числа
        numbers.sort()  # Сортирует числа в порядке возрастания
        print("Sorted numbers:", numbers)  # Выводит отсортированный список
    else:  # Иначе
        print("No numbers entered.")  # Выводит сообщение, что чисел не введено
    
    lib.GetFactorial()  # Получает и вычисляет факториал

if __name__ == "__main__":
    main()