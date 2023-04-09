import Models.Note


def write_file(array, mode):
    file = open("notes.txt", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.txt", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Models.Note.Note.to_string(notes))
        file.write('\n')
    file.close
