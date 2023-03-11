"""
cards game : Wizard
"""

from random import shuffle, choice

__author__ = "Pouria Keshtidar"


def create_cards():
    """
    create_cards: create a list of cards: 4 color, each one with 13 numbers.
    """
    number_dic = {11: "♙", 12: "♔", 13: "♛", 14: "A"}
    color_dic = {0: "♠", 1: "♥", 2: "♣", 3: "♦"}
    cards = []
    for color1 in range(4):  # range(4) because of 4 colors
        for number1 in range(2, 15):  # range(2,15)->cards number from 2 to 14
            if number1 < 11:  # create cards with number
                card1 = {str(number1): color_dic[color1]}
                cards.append(card1)
            else:  # create cards with characters
                card1 = {number_dic[number1]: color_dic[color1]}
                cards.append(card1)
    return cards  # return cards list


def deal_cards(round_number, cards, player_no):
    """
    :param round_number: number of the round, we are going to play.
    :param cards: cards list
    :param player_no: number of the players.
    """
    all_cards = []  # list of all players cards
    for _ in range(player_no):
        persons_card = []  # list of every player cards
        for _ in range(round_number):  # number of given cards is round_number
            persons_card.append(cards[0])  # add card to players cards_list
            cards.pop(0)  # delete the card from all cards
        all_cards.append(persons_card)  # add players cards_list to main_list
    all_cards_tuple = tuple(all_cards)  # change it from List to Tuple
    return all_cards_tuple  # return tasted list, players cards_lists


def compare_cards(cards, def_trumpfcolor, names1):
    """
    :param cards: players Chosen cards
    :param def_trumpfcolor: trumpfcolor of round
    :param names1: list of the players name.
    """
    number_dic = {"♙": 11, "♔": 12, "♛": 13, "A": 14}
    color_list = ["♠", "♥", "♣", "♦"]
    color_list.remove(def_trumpfcolor)  # remove the trumpfcolor
    val = [0 for _ in range(len(cards))]  # value table
    cards_colors = []  # color of the chosen cards
    cards_numbers = [0 for _ in range(len(cards))]  # all cards number
    for Quantity in range(len(cards)):  # all cards: number and symbol in lists
        for number2, color2 in cards[Quantity].items():
            print(number2, color2, "\t", end="")
            if number2.isdigit():
                cards_numbers[Quantity] = int(number2)
            else:
                cards_numbers[Quantity] = int(number_dic[number2])
            cards_colors.append(color2)
    for Quantity in range(len(cards)):  # Quantity = number of the Chosen cards
        if def_trumpfcolor in cards_colors:  # if we have trumpfcolor in cards
            for number3, color3 in cards[Quantity].items():
                if color3 == def_trumpfcolor:
                    if number3.isdigit():  # card value
                        val[Quantity] += int(number3)
                    else:
                        val[Quantity] += int(number_dic[number3])
                else:
                    val[Quantity] += 0  # another cards have 0 value
        # if all cards have same number.
        elif sum(cards_numbers) / len(cards_numbers) == max(cards_numbers):
            for number4, color4 in cards[Quantity].items():
                # cards with color of the first color in color list sub 0 val.
                if color4 == color_list[0]:
                    if number4.isdigit():
                        val[Quantity] += int(number4)
                    else:
                        val[Quantity] += int(number_dic[number4])
                # cards with color of the first color in color list sub 1 val.
                elif color4 == color_list[1]:
                    if number4.isdigit():
                        val[Quantity] += int(number4) - 1
                    else:
                        val[Quantity] += int(number_dic[number4]) - 1
                # cards with color of the first color in color list sub 2 val.
                elif color4 == color_list[2]:
                    if number4.isdigit():
                        val[Quantity] += int(number4) - 2
                    else:
                        val[Quantity] += int(number_dic[number4]) - 2
        # if cards numbers are not same, we will take value of the number.
        elif sum(cards_numbers) / len(cards_numbers) != max(cards_numbers):
            for number5, color5 in cards[Quantity].items():
                if number5.isdigit():
                    val[Quantity] += int(number5)
                else:
                    val[Quantity] += int(number_dic[number5])
    print("max:", max(val), "\t player: ", names1[val.index(max(val))], "\n")
    return val.index(max(val))  # return the index of max value


def emoj(nu):
    """
    param nu: number of the player
    return: each player name and emoji.
    """
    avatar = ""
    player_name = input("🧙\tPlayer " + nu +
                        " ,What's your name : ").capitalize()
    gender = ""
    while gender not in ("M", "W"):
        gender = input("🧙\tEnter Player " + nu + " gender (M/W): ").upper()
    if gender == "M":
        base = "y"
        while base not in ("A", "J", ""):
            base = input("🧙\tBase on age=A or job=J or nothing: ").upper()
        if base == "A":  # base Age
            while True:
                age = input("🧙\tHow old are you player " + nu + "? ")
                if age.isdigit():  # make sure user give number
                    age = int(age)
                    break
                else:
                    print("🧙\tPlease enter a number")
                    continue
            if 4 < age < 25:
                avatar = boys["boy"]
            elif 25 <= age <= 50:
                avatar = boys["sir"]
            elif age > 50:
                avatar = boys["Opa"]
            else:
                avatar = boys["baby"]
        elif base == "J":  # base job
            job = "0"
            print("1:Student\t 2:Astronaut\t 3:Programmer\t 4:Teacher"
                  "\t 5:Doctor\t 6:Koch\t 7:Police\t 8:Artist\t 9:Farmer"
                  "\t 10:mechanic")
            while job not in boys:
                job = input("🧙\tEnter number of job: ")
            avatar = boys[job]
        else:
            avatar = boys["prinz"]
    elif gender == "W":
        base = "y"
        while base not in ("A", "J", ""):
            base = input("🧙\tBase on age=A or job=J or nothing: ").upper()
        if base == "A":  # base Age
            while True:
                age = input("🧙\tHow old are you player " + nu + " ? ")
                if age.isdigit():  # make sure user give number
                    age = int(age)
                    break
                else:
                    print("🧙\tPlease enter a number")
                    continue
            if age < 25:
                avatar = girls["girl"]
            elif 25 <= age <= 50:
                avatar = girls["lady"]
            elif age > 50:
                avatar = girls["Oma"]
            else:
                avatar = girls["baby"]
        elif base == "J":  # base job
            job = "0"
            print("1:Student\t 2:Astronaut\t 3:Programmer\t 4:Teacher"
                  "\t 5:Doctor\t 6:Koch\t 7:Police\t 8:Artist\t 9:Farmer"
                  "\t 10:mechanic")
            while job not in girls:
                job = input("🧙\rEnter number of job: ")
            avatar = girls[job]
        else:
            avatar = girls["princess"]
    return player_name, avatar


boys = {"boy": "👦", "sir": "👨", "Opa": "👴", "prinz": "🤴",
        "1": "👨‍🎓", "2": "👨‍🚀", "3": "👨‍💻", "4": "👨‍🏫",
        "5": "👨‍⚕", "6": "👨‍🍳", "7": "👮‍",
        "8": "👨‍🎨", '9': "👨‍🌾", "10": "👨‍🔧", "baby": "👶"}
girls = {"girl": "👧", "lady": "👩", "Oma": "👵", "princess": "👸",
         "1": "👩‍🎓", "2": "👩‍🚀", '3': "👩‍💻", "4": "👩‍🏫",
         "5": "👩‍⚕", "6": "👩‍🍳", "7": "👮‍",
         "8": "👩‍🎨", "9": "👩‍🌾", "10": "👩‍🔧"}


if __name__ == '__main__':
    print("------------------------- All Cards ------------------------------")
    table = create_cards()
    for element in range(len(table)):  # print all cards ordered
        for number, color in table[element].items():
            print(number, color, "\t", end="")
        if (element + 1) % 13 == 0:
            print("\r")
    print("-----------------------------GAME---------------------------------")
    print("🧙\twe have a magic Game today!")
    print("we have key words, which you can type anytime and "
          "it will change the game Situation.(*please type the exact word*)\n"
          "1. new :if you want to start a new game."
          "\n2. end :if you  want to end the game. ")
    # game situation:  start = 1     new game = 0   exit = -1
    game_situation = 0
    win = []
    names = []
    while game_situation == 0:
        chosen_card = 0
        while True:
            pl_no = input("🧙\tEnter number of Players: ")  # player number
            if pl_no.isdigit():
                pl_no = int(pl_no)
                if 2 <= pl_no <= 5:  # check for the range of number
                    break
                else:
                    print("🧙\tPlease give number between 2 and 5!")
            else:
                print("🧙\tPlease give number between 2 and 5!")
        names = []  # names list
        for num in range(pl_no):  # get name and create Emoji
            player = emoj(str(num + 1))
            name = player[0] + " " + player[1]
            names.append(name)
            print("🧙\tWelcome ", name)
        win = [0 for _ in range(pl_no)]  # win Table
        game_situation = 1
        for round_num in range(1, int(52 / pl_no)):
            if game_situation == 1:
                print("\n\nRound number", round_num)
                table = create_cards()  # all cards
                shuffle(table)  # randomly mix cards
                # create card_Tuple
                cards_tuple = deal_cards(round_num, table, pl_no)
                dic3 = ["♠", "♥", "♣", "♦"]  # descending order of colors
                trumpfcolor = choice(dic3)  # random choice of trumpfcolor
                print("🧙\tTrump color: ", trumpfcolor, "\n")
                points = [0 for _ in range(pl_no)]  # card table to cal points
                for numb in range(round_num):
                    # print cards of each player with index
                    for name1 in range(pl_no):
                        print("🧙\tindex:(card)")
                        index_numb = 0
                        print(names[name1], end=" : ")
                        for card in cards_tuple[name1]:
                            for number, color in card.items():
                                index_numb += 1
                                if index_numb % 10 == 0:
                                    print("\r")
                                print(f"{index_numb}:", f"({number}{color})",
                                      end="    ")
                        print("\r")
                        while True:  # ask for Chosen_card Index
                            chosen_card = input("🧙\tEnter cards index: ")
                            if chosen_card.isdigit():
                                # accept if Index in range
                                chosen_card = int(chosen_card)
                                if 0 < int(chosen_card) < \
                                        (len(cards_tuple[name1]) + 1):
                                    break
                                else:
                                    print("Index out of Range")
                            elif chosen_card == "end" or chosen_card == "new":
                                break
                            else:
                                print("🧙\tplease Enter correct Index number")
                        if chosen_card == "end" or chosen_card == "new":
                            break
                        else:
                            points[name1] = cards_tuple[name1][chosen_card - 1]
                            cards_tuple[name1].pop(chosen_card - 1)
                            print("\n")
                    if chosen_card == "end":
                        game_situation = -1
                        break
                    elif chosen_card == "new":
                        game_situation = 0
                        print("\n\n\n")
                        break
                    else:
                        # winner card Index
                        inx = compare_cards(points, trumpfcolor, names)
                        win[inx] += 1  # add winner 1 in winner Table
            win.append(win[0])
            win.pop(0)
            names.append(names[0])
            names.pop(0)
        print("--------------------------------------------------------------")
        print("Point table: ", win)
        print("🧙\twinner: ", names[win.index(max(win))])
    print("------------------------------------------------------------------")
    print("🧙\tlittle price for the winner 😜")
    Drink = {1: "🍸", 2: "🍺", 3: "🍷", 4: "☕️", 5: "🥃"}  # cheers🥂
    Meal = {1: "🍔", 2: "🌭", 3: "🍕", 4: "🌮", 5: "🥗", 6: "🍣"}  # enjoy🍽
    Flower = {1: "🌻", 2: "🌹", 3: "🌷", 4: "🌼"}
    Sweets = {1: "🍫", 2: "🍰", 3: "🍦", 4: "🍭"}

    while True:
        price = input("Price:\nDrink=D  Meal=M  Flower=F  Sweet=S\nChar: ")\
            .upper()
        if price == "D":
            What = input("1=🍸\t2=🍺\t3=🍷\t4=☕\t5=🥃\nnum:  ")
            if What.isdigit():
                if int(What) in range(1, 6):
                    What = int(What)
                    print(f"Cheers{Drink[What]}", names[win.index(max(win))])
                    print("🧙 bye!👋")
                    break
                else:
                    print("🧙\tEnter a num from 1 to 5")
            else:
                print("🧙\tEnter a num from 1 to 5")
        elif price == "M":
            What = input("1=🍔\t2=🌭\t3=🍕\t4=🌮\t5=🥗\t6=🍣\nnum:  ")
            if What.isdigit():
                if int(What) in range(1, 7):
                    What = int(What)
                    print(f"Enjoy {Meal[What]}", names[win.index(max(win))])
                    print("🧙bye!👋")
                    break
                else:
                    print("🧙\tEnter a num from 1 to 6")
            else:
                print("🧙\tEnter a num from 1 to 6")
        elif price == "F":
            What = input("1=🌻\t2=🌹\t3=🌷\t4=🌼\nnum: ")
            if What.isdigit():
                if int(What) in range(1, 5):
                    What = int(What)
                    print(f"Enjoy {Flower[What]}", names[win.index(max(win))])
                    print("🧙bye!👋")
                    break
                else:
                    print("🧙\tEnter a num from 1 to 4")
            else:
                print("🧙\tEnter a num from 1 to 4")
        elif price == "S":
            What = input("1=🍫\t2=🍰\t3=🍦\t4=🍭\nnum: ")
            if What.isdigit():
                if int(What) in range(1, 5):
                    What = int(What)
                    print(f"Enjoy {Sweets[What]}", names[win.index(max(win))])
                    print("🧙bye!👋")
                    break
                else:
                    print("🧙\tEnter a num from 1 to 4")
            else:
                print("🧙\tEnter a num from 1 to 4")
        else:
            print("🧙\tPlease enter D or M or F or S")
