import os
import json

dirname = os.path.dirname(__file__)

filename = dirname + "\\notes.json"


def write_file(notes):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(notes, ensure_ascii=False))
    file.close


def read_file():
    try:
        print("Загружаем заметки из базы...")
        with open(filename, "r", encoding="utf-8") as file:
            notes = json.load(file)
        write_file(notes)
        file.close
        return notes
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Ошибка при загрузке файла JSON. Файл поврежден или имеет неверный формат.")
        return {}