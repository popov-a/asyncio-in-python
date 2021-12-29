import asyncio
import time

def blocking_io():
    print(f"Запуск `blocking_io()`: {time.strftime('%X')}")
    # Функция `time.sleep()` может быть заменена любой другой
    #  блокирующей операцией, например файловым вводом/выводом.
    time.sleep(1)
    print(f"Функция `blocking_io()` завершена: {time.strftime('%X')}")

async def main():
    print(f"Старт цикла событий: {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"Завершение цикла событий: {time.strftime('%X')}")

asyncio.run(main())

# Старт цикла событий: 09:33:04
# Запуск `blocking_io()`: 09:33:04
# Функция `blocking_io()` завершена: 09:33:05
# Завершение цикла событий: 09:33:05

# to_thread is only available in python 3.9+