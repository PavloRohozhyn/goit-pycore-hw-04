## Технiчний опис завдання

### Завдання 1
У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
Наприклад:
```
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```
Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

#### Вимоги до завдання:
- Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
- Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
- Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
- Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


### Завдання 2

У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:
```
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
````
Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

#### Вимоги до завдання:
- Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
- Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
- Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


### Завдання 3

Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

#### Вимоги до завдання:

- Створіть віртуальне оточення Python для ізоляції залежностей проекту.
- Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
- Використання бібліотеки colorama для реалізації кольорового виведення.
- Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
- Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.


### Завдання 4

Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.
У цій домашній роботі зосередимося на інтерфейсі самого бота. Найпростіший і найзручніший на початковому етапі розробки інтерфейс - це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати. 

Будь-який CLI складається з трьох основних елементів:
Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.
На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.

#### Вимоги до завдання:

- Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
- Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
- Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. В разі введення команди "exit" або "close", програма повинна завершувати виконання.
- Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
- Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
- Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.
- 
