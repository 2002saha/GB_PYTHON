import random


def shuffle_list(input_list):
    shuffled_list = []
    while input_list:
        # Выбираем случайный элемент из оставшихся в списке
        random_index = random.randint(0, len(input_list) - 1)
        # Добавляем его в перемешанный список и удаляем из исходного
        shuffled_list.append(input_list.pop(random_index))
    return shuffled_list


# Генерируем список
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Выводим исходный список
print("Исходный список:", input_list)

# Перемешиваем список
shuffled_list = shuffle_list(input_list)

# Выводим перемешанный список
print("Перемешанный список:", shuffled_list)
