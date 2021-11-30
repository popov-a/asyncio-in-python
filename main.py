import asyncio, time

async def say_after(delay, what):
    """Асинхронная функция (сопрограмма)"""
    await asyncio.sleep(delay)
    print(what)

async def main():
    """Точка входа в асинхронную программу"""
    print(f"started at {time.strftime('%X')}")
    print('ждем первую сопрограмму ...')
    await say_after(2, 'первый готов')

    # создаем задачи `task2` и `task3`
    print('запускаем задачи 2 и 3')
    task2 = asyncio.create_task(say_after(2, 'второй готов'))
    task3 = asyncio.create_task(say_after(4, 'третий готов'))

    # Ждем, пока обе задачи будут выполнены
    # (должно занять около 2 секунд.)
    print('ждем вторую задачу ...')
    await task2
    print('пауза на 5 сек ...')
    await asyncio.sleep(5)
    #await task3
    print(f"finished at {time.strftime('%X')}")

print('запускаем цикл событий')
asyncio.run(main())
print('продолжаем основную программу')