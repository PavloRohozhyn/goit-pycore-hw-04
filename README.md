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
