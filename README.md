
## Домашнее задание к занятию "30.2 Сериализаторы" Модуля 8 "Django REST framework" 

### Задача 1

В сериализатор для модели курса добавлено поле вывода количества уроков.



### Задача 2

Добавлена новая модель в приложение users:

#### Платежи

* <b>Пользователь</b>, ссылается на модель пользователя, который оплатил курс или урок.
* <b>Дата оплаты</b>,
* <b>Оплаченный курс или урок</b>, ссылается на модель курса или урока.
* <b>Сумма оплаты</b>,
* <b>Способ оплаты</b>: наличные или перевод на счет.

Создана фикстура с тестовыми данными для модели Платежи.


### Задача 3

Для сериализатора для модели курса реализовано дополнительное поле вывода уроков.


### Задача 4

Для эндпоинта вывода списка платежей настроена фильтрация по курс или урок и по способу оплаты.

1. Фильтрация по курсу
![filter_by_course](/media/readme/filter_by_course.png)

2. Фильтрация по уроку
![filter_by_lesson](/media/readme/filter_by_lesson2.png)

![filter_by_lesson](/media/readme/filter_by_lesson3.png)

3. Фильтрация по способу оплаты
![filter_by_cash](/media/readme/filter_by_cash.png)

4. Сортировка по дате (по возрастанию)
![sort_by_date](/media/readme/sort_by_date.png)

5. Сортировка по дате (по убыванию)
![sort_by_date](/media/readme/sort_by_date2.png)

6. Сортировка по дате и фильтрация по способу оплаты
![sort_by_date_and_filter_by_cash](/media/readme/sort_by_date_and_filter_by_cash.png)

7. Сортировка по дате, фильтрация по способу оплаты и поиск по имени пользователя
![sort_by_date_and_filter_by_cash_and_search_by_user](/media/readme/sort_by_date_and_filter_by_cash_and_search_by_user.png)

8. Сортировка по дате, фильтрация по способу оплаты и поиск по названию урока
![sort_by_date_and_filter_by_cash_and_search_by_lesson](/media/readme/sort_by_date_and_filter_by_cash_and_search_by_lesson.png)

9. Сортировка по дате и поиск по названию курса
![sort_by_date_and_search_by_course](/media/readme/sort_by_date_and_search_by_course.png)


### Задача 5

Дополнительно для профиля пользователя реализован вывод истории платежей.

![payment_history](/media/readme/payment_history.png)
