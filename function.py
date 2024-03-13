import file_operation as fo
import id
import ui
import time
from datetime import datetime


def add_note(notes):
    newNoteTitle = ui.check_len_text_input(input('Введите Название заметки: '))
    newNoteText = ui.check_len_text_input(input('Введите текст заметки: '))
    newNoteId = str(id.getNextId())
    
    notes[newNoteId] = {'id': newNoteId, 'noteTitle': newNoteTitle, 'noteText': newNoteText, 'noteDate': time.ctime(time.time())}
    fo.write_file(notes)
    print('Заметка успешна добавлена в файл.')


def show_notes(notes, choise):
    if(notes):
        if choise == 'all':
            for id in notes:
                print(f"№ {id}; {notes[id]['noteTitle']}; Дата: {notes[id]['noteDate']}")
                print(notes[id]['noteText'])
                print()
        if choise == 'id':
            id = input('Введите id заметки, которую хотите посмотреть: ')
            try:
                if id in notes:
                    print(f"Заметка № {id}: {notes[id]['noteTitle']}")
                    print(notes[id]['noteText'])
                    print()
                else:
                    print("Указанный id не найден.\n")
            except ValueError:
                print("Неверный ввод.\n")
        if choise == 'date':
            userDate = input('Введите дату в формате dd-mm-yyyy: ')
            choosenDate = datetime.strptime(userDate, "%d-%m-%Y").date()
            noNotesForTheDate = True
            for id in notes:
                noteDate = datetime.strptime(notes[id]['noteDate'], "%a %b %d %H:%M:%S %Y").date()
                if (noteDate == choosenDate):
                    noNotesForTheDate = False
                    print(f"Заметка № {id}: {notes[id]['noteTitle']}")
                    print(notes[id]['noteText'])
                    print()
            if noNotesForTheDate:
                print("Нет заметок за выбранную дату.")
    else:
        print('Заметок пока нет. Введите команду 1, чтобы добавить новую заметку.')


def change_note(notes, choise):
    choosenId = input('Введите id заметки: ')
    try:
        if choosenId in notes:
            if choise == 'edit':
                newNoteTitle = ui.check_len_text_input(input('Введите Название заметки: '))
                newNoteText = ui.check_len_text_input(input('Введите текст заметки: '))
                notes[choosenId]['noteTitle'] = newNoteTitle
                notes[choosenId]['noteText'] = newNoteText
                print('Заметка успешно изменена.')
            if choise == 'del':
                del notes[choosenId]
                print('Заметка успешно удалена.\n')
        else:
            print("Указанный id не найден.\n")
    except ValueError:
        print("Неверный ввод.\n")
    fo.write_file(notes)