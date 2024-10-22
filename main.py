inventory = ["тетрадка", "газета", "бутылка воды", "вафельная пушка"]
keys = set()
egg_given = False

levels = {
    1: "Лабиринт с тремя дорогами: налево, направо, прямо.",
    2: "Сражение с гигантом Никитой Кухельным.",
    3: "Рассмеши двух братьев - Никиты Макарова и Александра Пожарского.",
    4: "Король техникума Дубов Иван ждал вас."
        }

def show_inventory():
    print("Ваш инвентарь:", ", ".join(inventory))


def level_1():
    print(levels[1])
    print("Вы видите три дороги. Куда хотите пойти? (налево, направо, прямо)")
    choice = input("Ваш выбор: ").lower()
    if choice == "направо":
        print("Вы нашли ключ. Теперь он у вас.")
        keys.add("ключ")
    elif choice == "налево":
        if "ключ" in keys:
            print("Дверь открыта. Вы прошли на следующий уровень.")
        else:
            print("Дверь закрыта. Вам нужен ключ.")
            level_1()
            return
    else:
        print("Вы пошли прямо и вернулись назад.")
        level_1()


def level_2():
    global egg_given
    print(levels[2])
    print("Никита Кухельный готов к бою с вами. Выберите действие: потанцевать, драка на кулаках, вафельная пушка.")
    choice = input("Ваш выбор: ").lower()
    if choice == "вафельная пушка":
        print("Вы используете вафельную пушку! Никита смеется и отдает вам яйцо.")
        egg_given = True
    elif choice == "потанцевать":
        print("Вы отлично потанцевали! Никита смеется и отдает вам яйцо.")
        inventory.append("яйцо")
        egg_given = True
    else:
        print("Никита намного сильнее. Попробуйте еще раз.")
        level_2()

def level_3():
    print(levels[3])  ## Выводим описание уровня 3
    print("Выберите шутку, чтобы рассмешить братьев:")

    jokes = [
        "Золики",
        "Маленький золик",
        "Бульвар Дмитрия Донского"
    ]

    for i, joke in enumerate(jokes, start=1):
        print(f"{i}. {joke}")  #

    choice = int(input("Ваш выбор (1-3): ")) - 1
    if 0 <= choice < len(jokes):
        print("Братья смеются и пропускают вас!")
    else:
        print("Не смешно. Попробуйте еще раз.")
        level_3()


def level_4():
    print(levels[4])
    print("Какой предмет вы хотите отдать королю? Выберите из инвентаря:")
    show_inventory()
    item = input("Ваш выбор: ")
    if item in inventory:
        inventory.remove(item)
        print(f"Вы отдали {item} королю и покинули замок!")
    else:
        print("У вас нет такого предмета. Потрачено.")


def main():
    print("Добро пожаловать в техникум приключений!")
    show_inventory()
    level_1()
    level_2()
    level_3()
    level_4()
    print("Поздравляем вы завершили игру!")


if __name__ == "__main__":
    main()