import asyncio

async def cancel_me():
    print('cancel_me(): перед ожиданием')
    try:
        # ждем 1 час
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): отмена ожидания')
        # поднимаем еще раз
        # перехваченное исключение
        raise
    finally:
        print('cancel_me(): после ожидания')

async def main():
    # Создаем задачу для "cancel_me()"
    task = asyncio.create_task(cancel_me())

    # Ждем 1 сек.
    await asyncio.sleep(1)

    # Даем запрос на отмену
    task.cancel()

    await asyncio.sleep(5)

    #try:
    #    await task
    #except asyncio.CancelledError:
    #    print("main(): `cancel_me()` теперь отменен.")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): перед ожиданием
#     cancel_me(): отмена ожидания
#     cancel_me(): после ожидания
#     main(): cancel_me() теперь отменен.