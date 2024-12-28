import json, multiprocessing, threading
import time, gc # модуль Garbage Collector - осуществляет сборку мусора
import matplotlib.pyplot as plt




#  Работа с JSON или CPU-bound task. Скорость выполнения зависит от мощности процессора.
def job(parametr):                            # функция, принимающая кол-во элементов
    json.dumps(list(range(parametr)))         # генерирует список и превращает его в JSON


# Последовательный алгоритм sync будет выполнять тяжеловесную задачу N раз.
def serial(parametr, count):                # функция, принимающая кол-во элементов и количество повторений
    for _ in range(count):                  # Количество повторений
        job(parametr)                       # Последовательная функция, принимающая кол-во элементов

# Создадим по одному потоку на каждый вызов функции и попробуем добиться параллелизма
def threads_start(parametr, execution_Count):    # функция, принимающая кол-во элементов и количество повторений
    # создаем список потоков с функцией job и аргументом parametr с кол-м потоков равных "executionUnitsCount"
    threads = [threading.Thread(target=job, args=(parametr,)) for _ in range(execution_Count)]

    for thread in threads:     #запуск каждого потока из общего списка созданных потоков
        thread.start()

    for thread in threads:     #ожидаем завершения каждого запущенного потока
        thread.join()

# Создаем вместо потоков процессы
def processes_start(parametr, execution_Count): # функция, принимающая кол-во элементов и количество повторений
    # создаем список процессов с функцией job и аргументом parametr с кол-м процессов равных "executionUnitsCount"
    processes = [multiprocessing.Process(target=job, args=(parametr,)) for _ in range(execution_Count)]

    for process in processes:  #запуск каждого процесса из общего списка созданных процессов
        process.start()

    for process in processes:  #ожидаем завершения каждого запущенного процесса
        process.join()

x = []                                                    #список под задачи
y = []                                                    #общий список с результатами расчетов всеми способами
serial_result = []                                        #список с временами решения задач sync способом
threads_start_result = []                                 #список с временами решения задач способом multithreading
processes_start_result = []                               #список с временами решения задач способом multiprocessing


#Код тестирующий производительность всех реализаций:
if __name__ == '__main__':

    gc.disable()                                         #отключение автоматической сборки мусора
    jsonSize = 1000000                                   #кол-во аргументов

    # подставляем значения в кортеж при 10 итерациях  и получаем список из 10 кортежей
    box = [(jsonSize, i) for i in range(1, 11)]
    options = [serial, threads_start, processes_start]  #список функций:sync, multithreading, multiprocessing

    for i, q in enumerate(box):         #запуск 10 итераций кортежа для создания потоков от 1 до 10 и 1000000 аргументов
        parametr, execution_Count = q                                    #присвоение значений из кортежа объекта enumerate
        print(f"Кол-во задач: {execution_Count}, JSON размер: {parametr}")  #вывод кол-ва текущих задач и аргументов
        x.append(execution_Count)                                        #список с количеством задач - ось Х

        # функция, принимающая итерируемый объект и начальный индекс (0)
        for j, option in enumerate(options):
            start = time.perf_counter()                        #время начала работы программ
            option(parametr, execution_Count)                  #передача значений в наши программы
            end = time.perf_counter()                          #время окончания работы программ
            time_out = round(end - start, 2)                   #время работы программ
            print(f"Способ работы: {option.__name__}, время выполнения: {time_out} сек.")   #вывод значений в процессе решения
            if option.__name__ == 'serial':
                serial_result.append(time_out)            #отбор значений с временами решения задач sync способом
            if option.__name__ == 'threads_start':
                threads_start_result.append(time_out)     #отбор значений с временами решения задач способом multithreading
            if option.__name__ == 'processes_start':
                processes_start_result.append(time_out)   #отбор значений с временами решения задач способом multiprocessing

    print(serial_result)                                  #вывод списка с временами решения задач sync способом
    print(threads_start_result)                           #вывод списка с временами решения задач способом multithreading
    print(processes_start_result)                         #вывод списка с временами решения задач способом multiprocessing
    # График sync
    plt.plot(x, serial_result, label='sync', color='green', marker='o', markersize=7)
    # График multithreading
    plt.plot(x, threads_start_result, label='multithreading', color='blue', marker='o', markersize=7)
    # График multiproctssing
    plt.plot(x, processes_start_result, label='multiprocessing', color='red', marker='o', markersize=7)
    plt.legend(loc=0)                                               # Отображение названий графиков
    plt.xlabel('Количество задач')                                  # Подпись для оси х
    plt.ylabel('Время выполнения, сек.')                            # Подпись для оси y
    plt.title('График зависимостей CPU bound от способов решения')  # Название графика
    plt.grid(True)
    plt.show()



