import asyncio, time


async def worker(delay, name):
    # эмитируем ожидание какого-то ответа
    # ответа от стороннего сервиса
    await asyncio.sleep(delay)
    # возвращаем результат
    return name, delay


async def main():
    # список аргументов для `worker()``
    targets = [(0.5, 'one'), (0.8, 'two'),
               (0.2, 'three'), (1, 'four'), (0.5, 'five')]

    # создаем задачи
    tasks = [asyncio.create_task(worker(*target)) for target in targets]

    # передаем задачи в функцию `as_completed()`
    for future in asyncio.as_completed(tasks, timeout=1.1):
        # получаем результаты по готовности
        res = await future
        # выводим на печать
        print(f'Задача: {res[0]}; задержка: {res[1]}')


if __name__ == '__main__':
    start = time.time()
    # запускаем цикл событий
    asyncio.run(main())

    total = time.time() - start
    print(f'Общее время выполнения: {total:.3f} сек.')

# Задача: three; задержка: 0.2
# Задача: one; задержка: 0.5
# Задача: five; задержка: 0.5
# Задача: two; задержка: 0.8
# Задача: four; задержка: 1
# Общее время выполнения: 1.001 сек.