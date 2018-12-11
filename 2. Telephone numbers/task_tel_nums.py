def solution(s):
    # s - входная строка из описания задачи (https://github.com/evchibisova/contests/blob/master/2.%20Telephone%20numbers/desc_tel_nums.pdf)
    s = s.split("\n")
    # получаем список номеров клиентов. каждый номер - строка из цифр, например '123456'
    numbers = numbers_parser(s[1:int(s[0]) + 1])
    # получаем словарь шаблонов. ключ - все цифры номера без пробелов, X м других знаков, только цифры.
    # значение - список ["+код_страны код_оператора ", "персональный_номер", " - страна оператор",
    # длина номера (цифры + знаки X) с учетом кода страны и кода оператора, длина персонального номера (цифры + знаки X) без учета кода страны и кода оператора]
    # пример словаря: {'875291': ['28495': ['+28 (495) ', 'XXXXXXX', ' - ElDorado GoldLine', 12, 7]}
    patterns = patterns_parser(s[int(s[0]) + 2:])
    result = ""
    # проходим по всем номерам и всем шаблонам
    # считаем шаблон подходящим к номеру, если совпадают длина номера клиента и длина номера в шаблоне
    # и если совпадают цифры номера клиента и известные цифры номера в шаблоне
    # записываем полный вариант номера в result
    for number in numbers:
        for pattern in patterns:
            if len(number) == patterns[pattern][3] and pattern == number[:len(pattern)]:
                result += patterns[pattern][0] + number[-patterns[pattern][4]:] + patterns[pattern][2] + "\n"
                break
    result = result[:-1]  # удаляем последний \n
    return result


def numbers_parser(numbers):
    """удаляем из строк с телефонными номерами все символы, кроме цифр
    input: список номеров
    output: очищенный список номеров"""
    for i in range(len(numbers)):
        for sym in ["-", " ", "+", "(", ")"]:
            numbers[i] = numbers[i].replace(sym, "")
    return numbers


def patterns_parser(patterns):
    """превращаем строки щаблонов в словарь.
    input: список шаблонов
    output: словарь {цифры номера телефона: - страна оператор"""
    patterns_dict = dict()
    for pattern in patterns:
        country, oper, num = pattern.split()[:3]
        # создаем ключ из известных цифр кода страны, кода оператора и персонального номера
        key = country + oper + num
        for sym in ["-", " ", "+", "(", ")", "X"]:
            key = key.replace(sym, "")
        # значение - список ["+код_страны код_оператора ", "персональный_номер", " - страна оператор",
        # длина номера (цифры + знаки X) с учетом кода страны и кода оператора, длина номера (цифры + знаки X) без учета кода страны и кода оператора]
        patterns_dict[key] = ["{} {} ".format(country, oper),
                              num,
                              pattern[pattern.index("-")-1:],
                              len(key) + num.count("X"),
                              len(num)]
    print(patterns_dict)
    return patterns_dict

