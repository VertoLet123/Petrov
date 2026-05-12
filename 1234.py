person = {"name": "Алексей", "age": 20, "city": "Москва"}
if person["age"] >= 18:
    print(f"Совершеннолетний: {person['name']}")
else:
    print(f"Несовершеннолетний: {person['name']}")



numbers = [5, 12, 8, 21, 3, 15, 7]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)



scores = {
    "Анна": 85,
    "Борис": 47,
    "Вика": 92,
    "Глеб": 58,
    "Дима": 73
}
for name, score in scores.items():
    if score >= 60:
        print (f"{name}: {score}")


with open("numbers.txt", mode="r", encoding="utf-8") as file:
    lines = file.readlines()
    numbers_list = []
    total_sum = 0
for line in lines:
    number = int(line.strip())
    numbers_list.append(number)
    total_sum += number
print(total_sum)



stock = {
    "яблоки": 15,
    "бананы": 8,
    "апельсины": 0,
    "груши": 3,
    "киви": 0,
    "манго": 5
}
for name, value in stock.items():
    if value == 0:
        print(f"Товар {name} закончился")
    elif value < 10 and value > 0:
        print(f"Товар {name} осталось мало ({value} шт)")
    else:
        print(f"Товар {name} есть в наличии ({value} шт)")



numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
first_five = numbers[:5]
last_three = numbers[-3:]
every_second = numbers[::2]
print(first_five)
print(every_second)
print(last_three)



Задача на повторение №7 (темы: #while + условие + #break)
Напиши код, который:
Создаёт переменную number = 1
С помощью цикла #while выводит на экран текущее значение number
После вывода увеличивает number на 1
Цикл должен остановиться (#break), когда number достигнет значения 5 (то есть вывести числа 1, 2, 3, 4)
Вывод должен быть без использования условия #while number < 5 — остановку сделай именно через #break внутри цикла
Направление (без готового синтаксиса):
#break срабатывает внутри цикла при выполнении какого-то условия
Условие: если number == 5, то #break
Увеличение number — после вывода, до проверки на #break
Напиши код. Я проверю.

number = 1
while number < 5:
    print(number)
    number = number + 1
    if number == 5:
        break


Задача на повторение №8 (темы: файл + строки + методы .split() и .upper())
У тебя есть файл "message.txt" с таким содержимым (создай его вручную перед решением):
text
привет мир
это файл для задания
сегодня хороший день
Напиши код, который:

Открывает файл "message.txt" на чтение.
Читает его построчно.
Каждую строку переводит в верхний регистр (метод .upper()).
Каждую строку разбивает на слова (метод .split()) и выводит слова этой строки на экран, каждое слово с новой строки.
Пропускает пустые строки, если они есть.
Направление (без готового синтаксиса):
Открыть файл можно с with.
Читать построчно через цикл for line in file:.
Убрать лишние переносы строки (.strip()).
Если после .strip() строка пустая — пропустить (использовать if not line: #continue).
Применить .upper() к строке.
Применить .split() к строке — получится список слов.
Внутренним циклом пройти по этому списку и вывести каждое слово через print().

with open("message.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        line = line.upper().strip()
        if not line:
            continue
        words = line.split()
        for word in words:
            print(word)