import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    args = [('A', 2), ('B', 3), ('C', 4)]
    tasks = []
    for arg in args:
        # создаем задачи
        task = factorial(*arg)
        # складываем задачи в список
        tasks.append(task)

    # планируем одновременные вызовы
    all_result = await asyncio.gather(*tasks)
    print(all_result)
    return all_result


if __name__ == '__main__':
    # Запускаем цикл событий
    results = asyncio.run(main())
    print(results)

# Expected output:
#
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(2)...
#     Task C: Compute factorial(2)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24