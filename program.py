import function as f
import file_operation as fo
import ui


def run():
    input_from_user = ''
    notes = fo.read_file()
    while input_from_user != '7':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            f.add_note(notes)
        if input_from_user == '2':
            f.show_notes(notes, 'all')
            f.change_note(notes, 'edit')
        if input_from_user == '3':
            f.show_notes(notes, 'all')
        if input_from_user == '4':
            f.show_notes(notes, 'date')
        if input_from_user == '5':
            f.show_notes(notes, 'id')
        if input_from_user == '6':
            f.change_note(notes, 'del')
        if input_from_user == '7':
            ui.exit_program()
            break
