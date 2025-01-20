# Проект Python для сравнения моделей асинхронного программирования, демонстрирующих зависимость центрального процессорного устройства от нагрузки и влияние команд ввода/вывода
Данный проект позволяет продемонстрировать модели асинхронного программирования в двух вариантах:
в первом варианте - отражает зависимость центрального процессорного устройства от нагрузки, при решении заданного пользователем количества задач тремя методами: синхронным, с помощью потоков и с помощью процессов;
во втором варианте - отражает зависимость выполнения команд ввода/вывода, при решении заданного пользователем количества задач тремя методами: асинхронным (с помощью корутин), с помощью потоков и с помощью процессов.
## Содержание
- Технологии
- Настройка проекта
- Использование по назначению
- Обзор выполненной работы
- Команда проекта

## Технологии
- [PyCharm﻿](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone/)

## Настройка проекта
Для запуска проекта, необходимо выполнить предустановку PyCharm и открыть данный проект.
Установку можно произвести по ссылке выше из раздела Технологии.

Открыть файл, выбрав в левом верхнем углу File -> Open -> diplom.
![Открытие проекта](https://github.com/user-attachments/assets/27201b96-93a1-4f3b-94dd-901c918612de)
Рисуной 1. Начальная страница и открытие проекта.


Установите asyncio-пакет с помощью команды:
```sh
pip install asyncio
```
![Установка пакетов](https://github.com/user-attachments/assets/3418d494-f4fb-4e39-8c53-f64bdd33f475)
Рисунок 2. Установка пакетов для работы проекта.

Далее установка пакетов проходит аналогмчным способом, продемонстированном выше.

Установите multiprocessing-пакет с помощью команды:
```sh
pip install multiprocessing
```

Установите fastapi-пакет с помощью команды:
```sh
pip install fastapi
```

Установите pydantic-пакет с помощью команды:
```sh
pip install pydantic
```

Установите matplotlib-пакет с помощью команды:
```sh
pip install matplotlib
```

## Использование по назначению

### Тестирование выполнения CPU-bound задач
Для решения CPU-bound задач применяется 3 метода: синхронный, многопоточный и многопроцессный.\
При решении CPU-bound задач с помощью вышеуказанных методов можем подобрать их наибольшую эффективность под конкретное электронное устройство (персональный компьютер, планшет, сервер и т.п.). При хорошей аппаратной "начинке" наибольшей эффективности можно достичь многроцессным способом. При более "слабом" аппаратном устройстве многопоточный метод немного "шустрее", чем последовательный метод, но незначительно из-за ограничения GIL.\
Практически мы в этом убедимся, используя модуль multithreading_project.py
![Модуль multithreading_project](https://github.com/user-attachments/assets/411c8443-0dfe-4363-bd15-2f1d227caae5)
Рисунок 3. Модуль multithreading_project.py.

### Ввод данных для CPU-bound задач
В строке 71 в переменную jsonSize вводим (количество аргументов, над которыми проводится вычисления в наших методах). Чем больше значение, тем большую нагрузку даем для вычислений каждому методу, соответственно увеличивается время решения.
В строке 74 в метод range вводим количество задач, которые будут созданы и решены различными способами. \
range(начальное количество создаваемы задач, конечное количество создаваемы задач).

### Вывод данных: графики зависимостей количества задач и время выполнения для каждого метода
![Figure_1](https://github.com/user-attachments/assets/a926d745-ad7e-4944-b709-426f281413b0)
Рисунок 4. Вывод данных в виде грификов зависимостей.

Описание результата: при решении CPU bound задач в реализации на моем компьютере, наибольшей эффективности достиг многопоточный метод, хотя не на много лучше последовательного метода, из-за ограничения GIL. Хотя имея мощный компьютер, можно достичь значительного ускорения многопроцессного метода.


### Редактирование графика
В строке 116 реализован метод отображения на графике результата работы метода sync.\
В строке 118 реализован метод отображения на графике результата работы метода multithreading. \
В строке 120 реализован метод отображения на графике результата работы метода multiprocessing. \
Если результат не нужно отображать, то просто ее закомментируем, поставив в начале строки "#".

### Тестирование выполнения IO-bound задач
Для решения IO-bound задач применяется 3 метода: асинхронный(с помощью корутин), многопоточный и многопроцессный.\
При решении IO-bound задач с помощью вышеуказанных методов можем подобрать их наибольшую эффективность в работе с подсистемой ввода-вывода, а также устройствами с которыми мы взаимодействуем, например файловая система или сеть.\
Практически мы в этом убедимся, используя модуль in_output.py

### Ввод данных для IO-bound задач
В строке 51 в методе range вводим (начало диапазона количества задач; конец диапазона количества задач; шаг изменения количества задач)


###  Вывод данных: графики зависимостей количества задач и время выполнения для каждого метода
![Figure_4](https://github.com/user-attachments/assets/e3df5f5f-2c76-4701-af0e-5e6dc3c169d0)
Рисунок 5. Вывод данных: графики зависимостей количества задач и время выполнения для 3-х методов.

![Figure_2](https://github.com/user-attachments/assets/e944f0a6-dc7a-4f1c-8018-ced3a9ab0dcd)
Рисунок 6. Вывод данных: графики зависимостей количества задач и время выполнения для 2-х методов (корутины, многопоточность).

Описание результата: При решении IO-bound задач метод async (с помощью корутин), за счет того что ими управляет рантайм языка, а не ОС, и памяти нужно меньше, чем потоку является наилучшим вариантом. Чуть медленнее отработал многопоточный метод из-за взаимодействия с ОС, по сравнению с корутинами. Многопроцессность при решении таких задач не рекомендуется 
из-за необоснованности затрат ресурсов, без выигрыша в скорости по сравнению с многопоточностью и корутинами.

### Редактирование графика
В строке 83 реализован метод отображения на графике результата работы метода аsync.\
В строке 85 реализован метод отображения на графике результата работы метода multithreading. \
В строке 87 реализован метод отображения на графике результата работы метода multiprocessing. \
Если результат не нужно отображать, то просто ее закомментируем, поставив в начале строки "#".

### Обзор выполненной работы
Разработка проекта Python для сравнения моделей асинхронного программирования, демонстрирующих зависимость центрального процессорного устройства от нагрузки и влияние команд ввода/вывода успешно завершены в соответствии с изначально созданной документацией. Приложение включает функционал обработки генератора задач 
с использованием различных методов параллельной работы и графическим анализом результатов их работы. \
Реализованный проект соответствует требованиям и демонстрирует зависимость метода параллельной от работы от типа решаемых задач 
и технических характеристик компьютера.\
Методы параллельной работы действительно ускоряют процесс выполнения программы. Главное на этапе проектирования учесть все необходимые требования к вычислительным средствам, где разрабатываемое приложение будет использоваться и какие именно задачи будет решать.


## Команда проекта
- [Дмитрий Наседкин](tg://resolve?domain=@Dmitry_991) — PYTHON-разработчик urban-university


