import Repository.loadFromFile as lF
import Repository.writeToFile as wF
import Models.Note


def add_note():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Models.Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Models.Note.Note.get_id(note) == Models.Note.Note.get_id(i):
            Models.Note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Заметка добавлена в журнал")


def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("Журнал заметок:")
            for i in array_notes:
                print(Models.Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Models.Note.Note.get_id(i))
            id = input("Введите id заметки\n")
            flag = True
            for i in array_notes:
                if id == Models.Note.Note.get_id(i):
                    print(Models.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("введите дату в формате: dd.mm.yyyy:")
            flag = True
            for i in array_notes:
                date_note = str(Models.Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Models.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой")


def del_notes():
    id = input("Введите ID удаляемой заметки:")
    array_notes = lF.read_file()
    flag = False
    for i in array_notes:
        if id == Models.Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True
    if flag:
        print("Заметка с id: ", id, " успешно удалена")
    else:
        print("нет такого id")








