Задача №1 (Создание словаря)
Создайте словарь student с тремя парами ключ-значение:
ключ "name" → значение "Иван"
ключ "age" → значение 20
ключ "course" → значение "Python"
Выведите полученный словарь на экран.

student = {
    "name": "Иван" ,
    "age": 20 ,
    "course": "Python"
}
print(student)


Задача №2 (Доступ к элементам словаря по ключу)
Дан словарь:
person = {
    "first_name": "Анна",
    "last_name": "Смирнова",
    "city": "Москва"
}
Выведите на экран:
Значение по ключу "first_name"
Значение по ключу "city"

print(person["first_name"])
print(person["city"])


Задача №3 (Добавление и обновление элементов словаря)
Дан словарь:
user = {
    "login": "alex88",
    "email": "alex@mail.ru"
}
Выполните действия по порядку:
Добавьте новую пару "age": 25
Обновите значение ключа "email" на "alex_new@mail.ru"
Выведите итоговый словарь на экран

user["age"] = 25
user["email"] = "alex_new@mail.ru"
print(user)


Задача №4 (Удаление элементов словаря)
Дан словарь:
product = {
    "name": "ноутбук",
    "brand": "Lenovo",
    "price": 60000,
    "in_stock": True
}
Выполните действия:
Удалите ключ "price" с помощью оператора del
Удалите ключ "in_stock" с помощью метода pop() (сохраните удалённое значение в переменную и выведите её)
Выведите итоговый словарь

del product["price"]
in_stock = product.pop("in_stock")
print(in_stock)
print(product)


Задача №5 (Получение элементов, ключей и значений словаря)
Дан словарь:
book = {
    "title": "Мастер и Маргарита",
    "author": "Булгаков",
    "year": 1967,
    "genre": "роман"
}
Выведите на экран (каждый на отдельной строке):
Все ключи словаря (метод keys())
Все значения словаря (метод values())
Все пары ключ-значение в виде кортежей (метод items())

print(book.keys())
print(book.values())
print(book.items())


Задача №6 (Проверка на наличие ключей и значений)
Дан словарь:
python
phone = {
    "brand": "Samsung",
    "model": "Galaxy S23",
    "storage": 256
}
Выполните проверки и выведите результат (True или False):
Есть ли в словаре ключ "model"?
Есть ли в словаре ключ "color"?
Есть ли среди значений словаря значение 256? (используйте in вместе с values())
Есть ли среди значений словаря значение "iPhone"?

print("model" in phone)
print("color" in phone)
print(256 in phone.values())
print("iPhone" in phone.values())

