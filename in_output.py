import time
import asyncio
import concurrent.futures
import matplotlib.pyplot as plt

# Производительность зависит не от процессора, а от подсистемы ввода-вывода.
# Ввод/вывод будем имитировать с помощью sleep.
def job(parametr):
    time.sleep(parametr)

# Сделаем N вызовов функции последовательным способом выполнения задачи.
def serial(parametr, execution_Count):
    for _ in range(execution_Count):
        job(parametr)

async def async_job(parametr):
    await asyncio.sleep(parametr)

async def async_io_tasks(parametr, execution_Count):
    tasks = [asyncio.create_task(async_job(parametr)) for _ in range(execution_Count)]
    
    await asyncio.gather(*tasks)

# Конкурентная реализация на основе asyncio (корутинах).
def async_io_start(parametr, execution_Count):
    asyncio.run(async_io_tasks(parametr, execution_Count))

# Конкурентная реализация на потоках.
def threads_start(parametr, execution_Count):
    with concurrent.futures.ThreadPoolExecutor(max_workers=execution_Count) as executor:
        executor.map(job, [parametr] * execution_Count)

# Конкурентная реализация на процессах.
def processes_start(parametr, execution_Count):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(job, [parametr] * execution_Count)

# Список под задачи.
x = []
# Общий список с результатами расчетов всеми способами.
y = []
# Список с временами решения задач async способом.
async_io_start_result = []
# Список с временами решения задач способом multithreading.
threads_start_result = []
# Список с временами решения задач способом multiprocessing.
processes_start_result = []

# Сравним разницу между подходами, протестируя от 1 до 1001 конкурентных задач c шагом 200.
if __name__ == '__main__':
    box = [(0.1,  i) for i in range(1, 1002, 200)]
    options = [processes_start, threads_start, async_io_start]
    
    for i, q in enumerate(box):
        parametr, execution_Count = q
        print(f"Кол-во задач: {execution_Count}")
        x.append(execution_Count)
        
        for j, option in enumerate(options):
            start = time.perf_counter()
            option(parametr, execution_Count)
            end = time.perf_counter()
            time_out = round(end - start, 2)
            # Вывод значений в процессе решения.
            print(f"Способ работы: {option.__name__}, время выполнения: {time_out} сек.")
            if option.__name__ == 'async_io_start':
                # Отбор значений с временами решения задач async способом.
                async_io_start_result.append(time_out)
            if option.__name__ == 'threads_start':
                # Отбор значений с временами решения задач способом multithreading.
                threads_start_result.append(time_out)
            if option.__name__ == 'processes_start':
                # Отбор значений с временами решения задач способом multiprocessing.
                processes_start_result.append(time_out)

    # Вывод списка с временами решения задач async способом.
    print(async_io_start_result)
    # Вывод списка с временами решения задач способом multithreading.
    print(threads_start_result)
    # Вывод списка с временами решения задач способом multiprocessing.
    print(processes_start_result)
    # График async (корутин).
    plt.plot(x, async_io_start_result, label='async', color='green', marker='o', markersize=7)
    # График multithreading.
    plt.plot(x, threads_start_result, label='multithreading', color='blue', marker='o', markersize=7)
    # График multiprocessing.
    plt.plot(x, processes_start_result, label='multiprocessing', color='red', marker='o', markersize=7)
    # Отображение названий графиков.
    plt.legend(loc=0)
    # Название оси х.
    plt.xlabel('Количество конкурентных задач')
    # Название оси y.
    plt.ylabel('Время выполнения, сек.')
    # Название графика.
    plt.title('График зависимостей IO bound от способов решения')
    plt.grid(True)
    plt.show()
