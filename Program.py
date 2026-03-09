def main():
    print('Hello, World!')  # Печатает приветственное сообщение
    numbers = get_numbers()
    if numbers:
        numbers.sort()
        print("Sorted numbers:", numbers)
    else:
        print("No numbers entered.")

def get_numbers():
    numbers = []
    while True:
        value = input("Enter a number (or 'done' to finish): ")  # Запрашивает ввод числа или 'done' для завершения
        if value.lower() == 'done':
            break
        if value.isdigit() and int(value) > 0:
            numbers.append(int(value))
        else:
            print("Invalid input, please enter a positive integer.")
    return numbers

if __name__ == "__main__":
    main()