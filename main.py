def welcom():
    print(""" Привет, объясню правила игры!
    Ходить нужно по координатам, 1 координата это строка, 2 координата это столбец. Вот пример 1 2
    Вводить нужно только цифры через пробел, без запятых, точек и тд. Так же нельзя писать буквы!
    Удачи вам!""")

font = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(font):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def ask():
    while True:
        cords = input(' Ваш ход: ').split()
        if len(cords) != 2:
            print('Введите 2 числа')
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Числа не в дипозоне')
            continue

        if font[x][y] != " ":
            print('Клетка занята')
            continue
        return x, y

def win_checker():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(font[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            show()
            print("Выиграл 0!!!")
            return True
    return False



welcom()
show()

num = 0
while True:
    num += 1
    if num % 2 == 1:
        print('Ходит "X"')
    else:
        print("Ходит '0'")

    x, y = ask()

    if num % 2 == 1:
        font[x][y] = "X"
    else:
        font[x][y] = "0"

    if win_checker():
        break

    if num == 9:
        print('Ничья')
        show()
        break
    show()