Задача: создать имитацию системы маршрутных автобусов. Имеется список автобусных маршрутов, каждый маршрут содержит список станций и время проезда между ними. Также имеется список водителей, каждый из которых имеет имя и возраст. Необходимо:

Отфильтровать маршруты, время проезда по которым меньше 30 минут
Создать словарь, где ключом будет номер маршрута, а значением - список имен водителей, которые могут водить этот маршрут (водители старше 35 лет)
Используя Faker, для каждого маршрута генерировать случайное количество пассажиров (от 10 до 20 человек) и добавить их как свойство каждого маршрута