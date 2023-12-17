first_player_table = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'] for i in range(10)]
second_player_table = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'] for j in range(10)]

first_p_attack_table = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'] for k in range(10)]
second_p_attack_table = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'] for u in range(10)]

check_table_first = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'] for d in range(10)]
check_table_second = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'] for p in range(10)]

let_instead_num = {'A': '0', 'B': '1', 'C': "2", 'D': '3', 'E': "4", 'F': "5", 'G': "6", 'H': "7", 'I': "8", 'J': "9"}
col_let_num = [{'A': '0'}, {'B': '1'}, {'C': "2"}, {'D': '3'}, {'E': "4"}, {'F': "5"}, {'G': "6"}, {'H': "7"},
               {'I': "8"}, {'J': "9"}]

first_player_ship = [['9', '9', '9'], ['0', '0', '0', '0']]
second_player_ships = [['9', '9', '9'], ['0', '0', '0', '0']]

list_pos_5_1 = []
list_pos_6_1 = []
list_pos_7_1 = []
list_pos_8_1 = []
list_pos_9_1 = []
list_pos_0_1 = []

list_pos_5_2 = []
list_pos_6_2 = []
list_pos_7_2 = []
list_pos_8_2 = []
list_pos_9_2 = []
list_pos_0_2 = []


def show_ships(list_of_ships):
    for i in list_of_ships:
        for j in i:
            print(j, end=" ")
        print()


def check_boarders(table, start_point):
    boarders_mark = '#'
    square_boarders = [(0, 0), (0, 1), (1, 0), (0, -1), (0, -1), (-1, 0), (-1, 0), (0, 1), (0, 1)]
    table[start_point[0]][start_point[1]] = boarders_mark
    for i in square_boarders:
        i_0 = i[0]
        i_1 = i[1]
        start_point[0] = start_point[0] + i_0
        start_point[1] = start_point[1] + i_1
        if 0 <= start_point[0] <= 9 and 0 <= start_point[1] <= 9:
            table[start_point[0]][start_point[1]] = boarders_mark
        else:
            continue


def show_table(elements):
    res = "  "
    for i in range(len(col_let_num)):
        res += list(col_let_num[i].keys())[0] + ' '
    print(res)
    for i in range(10):
        res_2 = str(i) + '|'
        for j in range(len(elements[i])):
            res_2 += f"{elements[i][j]}{' '}"
        print(res_2)


flag_of_rem_ship = True


def put_ship(ship, check_putting_table, table):
    print("Введите начальную и конечнюю точку координаты!")
    print("Если же корабль однопалубный, то одну координату!")
    try:
        coordinates = input().upper().split()
        global flag_of_rem_ship
        if len(ship) == 1 and len(coordinates) == 1:
            column, row = coordinates[0][0], coordinates[0][1]
            if check_putting_table[int(row)][int(let_instead_num[column])] == "*":
                table[int(row)][int(let_instead_num[column])] = ship[0]
            else:
                print('Нельзя ставить корабль возле другого корабля!')
                flag_of_rem_ship = False
                return flag_of_rem_ship
            check_boarders(check_putting_table, [int(row), int(let_instead_num[column])])
        elif len(coordinates) == 2:
            column_letter_1, row_num_1 = coordinates[0][0], coordinates[0][1]
            column_letter_2, row_num_2 = coordinates[1][0], coordinates[1][1]
            if column_letter_1 == column_letter_2:
                if abs(int(row_num_1) - int(row_num_2)) + 1 != len(ship):
                    print('Введены неверные координаты!')
                    flag_of_rem_ship = False
                    return flag_of_rem_ship
                start = int(row_num_1)
                position_of_ship = []
                for i in range(start, start + len(ship)):
                    if check_putting_table[int(i)][int(let_instead_num[column_letter_1])] == "*":
                        position_of_ship.append(list([int(i), int(let_instead_num[column_letter_1])]))
                    else:
                        print('Нельзя ставить корабль возле другого корабля!')
                        flag_of_rem_ship = False
                        return flag_of_rem_ship
                for i in position_of_ship:
                    table[i[0]][i[1]] = ship[0]
                check_boarders(check_putting_table, [start, int(let_instead_num[column_letter_1])])
                check_boarders(check_putting_table, [start + len(ship) - 1, int(let_instead_num[column_letter_1])])
            elif column_letter_1 != column_letter_2:
                if abs(int(let_instead_num[column_letter_1]) - int(let_instead_num[column_letter_2])) + 1 != len(ship) \
                        and row_num_1 == row_num_2:
                    print('Введены неверные координаты!')
                    flag_of_rem_ship = False
                    return flag_of_rem_ship
                elif row_num_1 != row_num_2:
                    flag_of_rem_ship = False
                    return flag_of_rem_ship
                start = int(let_instead_num[column_letter_1])
                position_of_ship = []
                for i in range(start, start + len(ship)):
                    if check_putting_table[int(row_num_1)][i] == "*":
                        position_of_ship.append(list([int(row_num_1), i]))
                    else:
                        print('Нельзя ставить корабль возле другого корабля!')
                        flag_of_rem_ship = False
                        return flag_of_rem_ship
                for i in position_of_ship:
                    table[i[0]][i[1]] = ship[0]
                check_boarders(check_putting_table, [int(row_num_1), start])
                check_boarders(check_putting_table, [int(row_num_1), start + len(ship) - 1])
            flag_of_rem_ship = True
    except Exception:
        print('Попробуй снова, что то пошло не так')
        flag_of_rem_ship = False


def check_ship(list_of_ship, check_table, table):
    player_status = True
    while player_status:
        print('Ваши корабли:')
        show_ships(list_of_ship)
        show_table(table)
        choice = input('Введите корабль который хотите поставить: ').split()
        if choice not in list_of_ship:
            print('У вас нет токого корабля')
            continue
        put_ship(choice, check_table, table)
        if choice in list_of_ship and flag_of_rem_ship is True:
            list_of_ship.remove(choice)
        if not list_of_ship:
            show_table(table)
            player_status = False


def check_hits(table_to_attack, player_table, list_5, list_6, list_7, list_8, list_9, list_0):
    coordinates = input('Введите координаты: ').upper().split()
    column = coordinates[0][0]
    row = coordinates[0][1]
    if table_to_attack[int(row)][int(let_instead_num[column])] == '#' or table_to_attack[int(row)][int(let_instead_num[column])] == 'X':
        print('Вы уже стреляли в эти координаты!')
        return check_hits(table_to_attack, player_table, list_5, list_6, list_7, list_8, list_9, list_0)
    if player_table[int(row)][int(let_instead_num[column])] == "1" or player_table[int(row)][int(let_instead_num[column])] == "2" or player_table[int(row)][int(let_instead_num[column])] == "3" or player_table[int(row)][int(let_instead_num[column])] == "4":
        check_boarders(table_to_attack, [int(row), int(let_instead_num[column])])
        table_to_attack[int(row)][int(let_instead_num[column])] = 'X'
        show_table(table_to_attack)
        print('Бум!')
        print('Корабль уничтожен!')
        return ['hitted', -1]
    if player_table[int(row)][int(let_instead_num[column])] == "5":
        list_5.append(coordinates)
        if len(list_5) == 2:
            check_boarders(table_to_attack, [int(list_5[0][0][1]), int(let_instead_num[list_5[0][0][0]])])
            check_boarders(table_to_attack, [int(list_5[1][0][1]), int(let_instead_num[list_5[1][0][0]])])
            table_to_attack[int(list_5[0][0][1])][int(let_instead_num[list_5[0][0][0]])] = 'X'
        table_to_attack[int(row)][int(let_instead_num[column])] = 'X'
        show_table(table_to_attack)
        print('Бум!')
        return ['hitted', 5]
    if player_table[int(row)][int(let_instead_num[column])] == "6":
        list_6.append(coordinates)
        if len(list_6) == 2:
            check_boarders(table_to_attack, [int(list_6[0][0][1]), int(let_instead_num[list_6[0][0][0]])])
            check_boarders(table_to_attack, [int(list_6[1][0][1]), int(let_instead_num[list_6[1][0][0]])])
            table_to_attack[int(list_6[0][0][1])][int(let_instead_num[list_6[0][0][0]])] = 'X'
        table_to_attack[int(row)][int(let_instead_num[column])] = 'X'
        show_table(table_to_attack)
        print('Бум!')
        return ['hitted', 6]
    if player_table[int(row)][int(let_instead_num[column])] == "7":
        list_7.append(coordinates)
        if len(list_7) == 2:
            check_boarders(table_to_attack, [int(list_7[0][0][1]), int(let_instead_num[list_7[0][0][0]])])
            check_boarders(table_to_attack, [int(list_7[1][0][1]), int(let_instead_num[list_7[1][0][0]])])
            table_to_attack[int(list_7[0][0][1])][int(let_instead_num[list_7[0][0][0]])] = 'X'
        table_to_attack[int(row)][int(let_instead_num[column])] = 'X'
        show_table(table_to_attack)
        print('Бум!')
        return ['hitted', 7]
    if player_table[int(row)][int(let_instead_num[column])] == "8":
        list_8.append(coordinates)
        if len(list_8) == 3:
            check_boarders(table_to_attack, [int(list_8[0][0][1]), int(let_instead_num[list_8[0][0][0]])])
            check_boarders(table_to_attack, [int(list_8[-1][0][1]), int(let_instead_num[list_8[-1][0][0]])])
            table_to_attack[int(list_8[0][0][1])][int(let_instead_num[list_8[0][0][0]])] = 'X'
            table_to_attack[int(list_8[1][0][1])][int(let_instead_num[list_8[1][0][0]])] = 'X'
        table_to_attack[int(row)][int(let_instead_num[column])] = 'X'
        show_table(table_to_attack)
        print('Бум!')
        return ['hitted', 8]
    if player_table[int(row)][int(let_instead_num[column])] == "9":
        list_9.append(coordinates)
        if len(list_9) == 3:
            check_boarders(table_to_attack, [int(list_9[0][0][1]), int(let_instead_num[list_9[0][0][0]])])
            check_boarders(table_to_attack, [int(list_9[-1][0][1]), int(let_instead_num[list_9[-1][0][0]])])
            table_to_attack[int(list_9[0][0][1])][int(let_instead_num[list_9[0][0][0]])] = 'X'
            table_to_attack[int(list_9[1][0][1])][int(let_instead_num[list_9[1][0][0]])] = 'X'
        table_to_attack[int(row)][int(let_instead_num[column])] = 'X'
        show_table(table_to_attack)
        print('Бум!')
        return ['hitted', 9]
    if player_table[int(row)][int(let_instead_num[column])] == "0":
        list_0.append(coordinates)
        if len(list_0) == 4:
            check_boarders(table_to_attack, [int(list_0[0][0][1]), int(let_instead_num[list_0[0][0][0]])])
            check_boarders(table_to_attack, [int(list_0[-1][0][1]), int(let_instead_num[list_0[-1][0][0]])])
            table_to_attack[int(list_0[0][0][1])][int(let_instead_num[list_0[0][0][0]])] = 'X'
            table_to_attack[int(list_0[1][0][1])][int(let_instead_num[list_0[1][0][0]])] = 'X'
            table_to_attack[int(list_0[2][0][1])][int(let_instead_num[list_0[2][0][0]])] = 'X'
        table_to_attack[int(row)][int(let_instead_num[column])] = 'X'
        show_table(table_to_attack)
        print('Бум!')
        return ['hitted', 0]
    if player_table[int(row)][int(let_instead_num[column])] == '*':
        table_to_attack[int(row)][int(let_instead_num[column])] = '#'
        show_table(table_to_attack)
        print('Промах!')
        return ['missed', -1]


def sea_battle():
    print('Пришло время атаковать!')
    count_first_hits = 0
    count_second_hits = 0
    game_status = True
    list_5_1, list_6_1, list_7_1, list_8_1, list_9_1, list_0_1, list_5_2, list_6_2, list_7_2, list_8_2, list_9_2, \
        list_0_2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    while game_status:
        while count_first_hits != 7:
            print('Очередь первого игрока!')
            checking_game = check_hits(first_p_attack_table, second_player_table, list_pos_5_1, list_pos_6_1, list_pos_7_1, list_pos_8_1, list_pos_9_1, list_pos_0_1)
            if checking_game[1] == 5:
                list_5_1 += 1
            if checking_game[1] == 6:
                list_6_1 += 1
            if checking_game[1] == 7:
                list_7_1 += 1
            if checking_game[1] == 8:
                list_8_1 += 1
            if checking_game[1] == 9:
                list_9_1 += 1
            if checking_game[1] == 0:
                list_0_1 += 1
            if list_5_1 == 2:
                print('Корабль подбит!')
                list_5_1 -= 1
            if list_6_1 == 2:
                print('Корабль подбит!')
                list_6_1 -= 1
            if list_7_1 == 2:
                print('Корабль подбит!')
                list_7_1 -= 1
            if list_8_1 == 3:
                print('Корабль подбит!')
                list_8_1 -= 1
            if list_9_1 == 3:
                print('Корабль подбит!')
                list_9_1 -= 1
            if list_0_1 == 4:
                print('Корабль подбит!')
                list_0_1 -= 1
            if checking_game[0] == 'hitted':
                count_first_hits += 1
                continue
            elif checking_game[0] == 'missed':
                break
        if count_first_hits == 7:
            print('Первый игрок победил!')
            game_status = False
            continue
        while count_second_hits != 7:
            print('Очередь второго игрока!')
            checking_game = check_hits(second_p_attack_table, first_player_table, list_pos_5_2, list_pos_6_2, list_pos_7_2, list_pos_8_2, list_pos_9_2, list_pos_0_2)
            if checking_game[1] == 5:
                list_5_2 += 1
            if checking_game[1] == 6:
                list_6_2 += 1
            if checking_game[1] == 7:
                list_7_2 += 1
            if checking_game[1] == 8:
                list_8_2 += 1
            if checking_game[1] == 9:
                list_9_2 += 1
            if checking_game[1] == 0:
                list_0_2 += 1
            if list_5_2 == 2:
                print('Корабль подбит!')
                list_5_2 -= 1
            if list_6_2 == 2:
                print('Корабль подбит!')
                list_6_2 -= 1
            if list_7_2 == 2:
                print('Корабль подбит!')
                list_7_2 -= 1
            if list_8_2 == 3:
                print('Корабль подбит!')
                list_8_2 -= 1
            if list_9_2 == 3:
                print('Корабль подбит!')
                list_9_2 -= 1
            if list_0_2 == 4:
                print('Корабль подбит!')
                list_0_2 -= 1
            if checking_game[0] == 'hitted':
                count_second_hits += 1
                continue
            elif checking_game[0] == 'missed':
                break
        if count_second_hits == 7:
            print('Второй игрок победил')
            game_status = False
            continue


print(f'Выбирает первый игрок!')
check_ship(first_player_ship, check_table_first, first_player_table)

print(f'Выбирает второй игрок!')
check_ship(second_player_ships, check_table_second, second_player_table)

sea_battle()
