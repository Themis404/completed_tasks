'''4. Дан список результатов попыток
одного спортсмена для некоторого соревнования.
Написать функцию, которая считает
сколько за сессию был установлен новый рекорд,
т.е. текущее значение превышает значение максимального.

Например
Имеем список результатов.:

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1].

В данном случае ответ: 2.
'''
def maxRecord(results, bestResults):

    records = results[0]
    for res in results:
        if res > records:
            records = res
            bestResults.append(records)
    return bestResults

def maxAmount(bestResults):

    amount = len(bestResults)
    return amount

def main():

    bestResults = []
    results = [12, 23, 34, 23, 44, 1, 32]
    print("Все результаты спортсмена: ", results)
    print("Лучшие результаты: ",maxRecord(results, bestResults))
    print("Количесво лучших попыток: ", maxAmount(bestResults))


if __name__ == '__main__':
    main()