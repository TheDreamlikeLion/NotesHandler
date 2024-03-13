import file_operation as fo

notes = fo.read_file()
id = len(notes)

def getNextId():
    global id
    id+=1
    return id