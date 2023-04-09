import UI.menuTemplates as m


def menu_console():
        m.printNenuTitle("Главное меню\n           Журнал заметок")
        print("1 - вывод всех заметок \n2 - вывод заметки по id \n3 - выбор заметок по дате\n4 - редактирование заметки"
              " \n5 - добавление заметки\n6 - удаление заметки\n7 - выход")
        m.printMenuLine()
        print("\n введите пункт из меню ")


