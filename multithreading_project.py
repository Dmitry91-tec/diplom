import json
import multiprocessing
import threading
import time
# модуль Garbage Collector - осуществляет сборку мусора.
import gc
import matplotlib.pyplot as plt


# Работа с JSON или CPU-bound task. Скорость выполнения зависит от мощности процессора.
# Функция job, принимающая количество элементов.
def job(parametr):
    # генерирует список и превращает его в JSON
    json.dumps(list(range(parametr)))


# Последовательный алгоритм sync будет выполнять преобразование списка в строку формата JSON N раз.
# Функция serial, принимающая количество элементов и количество повторений.
def serial(parametr, count):
    # Количество повторений.
    for _ in range(count):
        # Последовательная функция, принимающая количество элементов.
        job(parametr)

# Создадим по одному потоку на каждый вызов функции и попробуем добиться параллелизма.
# Функция, принимающая количество элементов и количество повторений.
def threads_start(parametr, execution_Count):
    # Создаем список потоков с функцией job и аргументом parametr с количеством потоков равных "executionUnitsCount".
    threads = [threading.Thread(target=job, args=(parametr,)) for _ in range(execution_Count)]

    # Запуск каждого потока из общего списка созданных потоков.
    for thread in threads:
        thread.start()

    # Ожидаем завершения каждого запущенного потока.
    for thread in threads:
        thread.join()

# Создаем вместо потоков процессы.
# Функция, принимающая кол-во элементов и количество повторений.
def processes_start(parametr, execution_Count):
    # Создаем список процессов с функцией job и аргументом parametr с количеством процессов равных "execution_Count".
    processes = [multiprocessing.Process(target=job, args=(parametr,)) for _ in range(execution_Count)]

    # Запуск каждого процесса из общего списка созданных процессов.
    for process in processes:
        process.start()

    # Ожидаем завершения каждого запущенного процесса.
    for process in processes:
        process.join()

# Список под задачи.
x = []
# Общий список с результатами расчетов всеми способами.
y = []
# Список с временами решения задач sync способом.
serial_result = []
# Список с временами решения задач способом multithreading.
threads_start_result = []
# Список с временами решения задач способом multiprocessing.
processes_start_result = []


#Код тестирующий производительность всех реализаций:
if __name__ == '__main__':

    # Отключение автоматической сборки мусора.
    gc.disable()
    # Количество аргументов.
    jsonSize = 1000000

    # Подставляем значения в кортеж при 10 итерациях  и получаем список из 10 кортежей.
    box = [(jsonSize, i) for i in range(1, 11)]
    # Список функций: sync, multithreading, multiprocessing.
    options = [serial, threads_start, processes_start]

    # Запуск 10 итераций кортежа для создания потоков от 1 до 10 и 1000000 аргументов.
    for i, q in enumerate(box):
        # Присвоение значений из кортежа объекта enumerate.
        parametr, execution_Count = q
        # Вывод количества текущих задач и аргументов.
        print(f"Кол-во задач: {execution_Count}, JSON размер: {parametr}")
        # Список с количеством задач - ось Х.
        x.append(execution_Count)

        # Функция, принимающая итерируемый объект и начальный индекс (0).
        for j, option in enumerate(options):
            # Время начала работы программы.
            start = time.perf_counter()
            # Передача значений в наши методы программирования.
            option(parametr, execution_Count)
            # Время окончания работы программы.
            end = time.perf_counter()
            # Время работы метода программирования.
            time_out = round(end - start, 2)
            # Вывод значений в процессе решения
            print(f"Способ работы: {option.__name__}, время выполнения: {time_out} сек.")
            if option.__name__ == 'serial':
                # Отбор значений с временами решения задач sync способом.
                serial_result.append(time_out)
            if option.__name__ == 'threads_start':
                # Отбор значений с временами решения задач способом multithreading.
                threads_start_result.append(time_out)
            if option.__name__ == 'processes_start':
                # Отбор значений с временами решения задач способом multiprocessing.
                processes_start_result.append(time_out)

    # Вывод списка с временами решения задач sync способом.
    print(serial_result)
    # Вывод списка с временами решения задач способом multithreading.
    print(threads_start_result)
    # Вывод списка с временами решения задач способом multiprocessing.
    print(processes_start_result)
    # График sync.
    plt.plot(x, serial_result, label='sync', color='green', marker='o', markersize=7)
    # График multithreading.
    plt.plot(x, threads_start_result, label='multithreading', color='blue', marker='o', markersize=7)
    # График multiproctssing.
    plt.plot(x, processes_start_result, label='multiprocessing', color='red', marker='o', markersize=7)
    # Отображение названий графиков.
    plt.legend(loc=0)
    # Название оси х.
    plt.xlabel('Количество задач')
    # Название оси y.
    plt.ylabel('Время выполнения, сек.')
    # Название графика.
    plt.title('График зависимостей CPU bound от способов решения')
    plt.grid(True)
    plt.show()



