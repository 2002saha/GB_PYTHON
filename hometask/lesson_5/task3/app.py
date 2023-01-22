import os
from time import sleep

def compress(input_file, output_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(current_dir, "log.txt")
    with open(input_file, "r") as in_file:
        data = in_file.read()
    compressed = ""
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed += str(count) + current_char
            current_char = char
            count = 1
    compressed += str(count) + current_char

    with open(output_file, "w") as out_file:
        out_file.write(compressed)

    with open(log_file, "a") as log:
        log.write(f"{data} was compressed to {compressed}\n")
    print("status: Сжатие данных успешно выполнено.")

def decompress(input_file, output_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(current_dir, "log.txt")
    with open(input_file, "r") as in_file:
        data = in_file.read()
    decompressed = ""
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        else:
            if count:
                decompressed += int(count) * char
                count = ""
            else:
                decompressed += char
    with open(output_file, "w") as out_file:
        out_file.write(decompressed)
    
    with open(log_file, "a") as log:
        log.write(f"{data} was decompressed to {decompressed}\n")
    print("status: Восстановления данных успешно выполнено.")

def create_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")
    output_file = os.path.join(current_dir, "output.txt")
    log_file = os.path.join(current_dir, "log.txt")
    open(input_file, "w").close()
    open(output_file, "w").close()
    open(log_file, "w").close()
    print("status: Файлы успешено созданы.")

def info():
    print("Эта автоматическая программа сжатия и восстановления данных. Ведёт истории в файл log.txt . Автор: Полежаев Александр")

def clear_files(input_file, output_file):
    with open(input_file, "w") as in_file:
        in_file.write("")
    with open(output_file, "w") as out_file:
        out_file.write("")
    print("status: input.txt и output.txt успешно очищены.")

def main():
    delay = 2
    while True:
        print("Выберите опцию:")
        print("1. Сжать")
        print("2. Восстановление")
        print("3. Создание входных и выходных файлов (обязательно при первом запуске)")
        print("4. Очистка входных и выходных файлов")
        print("5. Информация")
        print("6. Выход")
        choice = int(input("Выберите опцию: "))
        current_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(current_dir, "input.txt")
        output_file = os.path.join(current_dir, "output.txt")
        if choice == 1:
            compress(input_file, output_file)
            print()
        elif choice == 2:
            decompress(input_file, output_file)
            print()
        elif choice == 3:
            create_files()
            print()
        elif choice == 4:
            clear_files(input_file, output_file)
            print()
        elif choice == 6:
            print("Выход из программы..")
            sleep(delay)
            os.system('cls')
            break
        elif choice == 5:
            info()
            print()
        else:
            print("Выбран недопустимый вариант")
            print()

if __name__ == "__main__":
    main()
