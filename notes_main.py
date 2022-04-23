from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLineEdit, QListWidget, QVBoxLayout, QHBoxLayout, QLabel, QInputDialog
import json

with open('notes.json', 'r') as data:
    notes = json.load(data)

app = QApplication([])
wind = QWidget()
wind.setWindowTitle('Smart Notes')

Nlabal = QLabel('Notes')
Ntext_edit = QTextEdit()
Nlist = QListWidget()
Ncreate_but = QPushButton('create note')
Ndelete_but = QPushButton('delete note')
Nsave_but = QPushButton('save note')
teg_label = QLabel('tags')
teg_list = QListWidget()
teg_input = QLineEdit()
teg_add_but = QPushButton('add teg')
teg_delete_but = QPushButton('delete tag')
Ntag_browse_but = QPushButton('Browse notes by tags')

main_line = QHBoxLayout()
raight_main_line = QVBoxLayout()
Nline = QHBoxLayout()
tag_line = QHBoxLayout()
Nline.addWidget(Ncreate_but)
Nline.addWidget(Ndelete_but)
tag_line.addWidget(teg_add_but)
tag_line.addWidget(teg_delete_but)
raight_main_line.addWidget(Nlabal)
raight_main_line.addWidget(Nlist)
raight_main_line.addLayout(Nline)
raight_main_line.addWidget(Nsave_but)
raight_main_line.addWidget(teg_label)
raight_main_line.addWidget(teg_list)
raight_main_line.addWidget(teg_input)
raight_main_line.addLayout(tag_line)
raight_main_line.addWidget(Ntag_browse_but)
main_line.addWidget(Ntext_edit)
main_line.addLayout(raight_main_line)
wind.setLayout(main_line)
wind.show()

def Nshow(item):
    for name in notes:
        if name["name"] == item.text():
            note = name
    teg_list.clear()
    for tag in note["tags"]:
        teg_list.addItem(tag)
    Ntext_edit.setText(note["text"])

def Nadd():
    Nname, ok = QInputDialog.getText(wind, "note name", "note name")
    if ok and Nname != "":
        notes.append({"name":Nname, "tags":[], "text":""})
        with open("notes.json", "w") as filer:
            json.dump(notes, filer)
        Nlist.addItem(Nname)
        teg_list.clear()
        Ntext_edit.clear()

def Ndel():
    name = Nlist.selectedItems()[0].text()
    for note in notes:
        if note["name"] == name:
            index = notes.index(note)
    del notes[index]
    with open("notes.json", "w") as filer:
        json.dump(notes, filer)
    Nlist.clear()
    for note in notes:
        Nlist.addItem(note["name"])
    teg_list.clear()
    Ntext_edit.clear()

def Nsave():
    name = Nlist.selectedItems()[0].text()
    for note in notes:
        if note["name"] == name:
            note["text"] = Ntext_edit.toPlainText()
    with open("notes.json", "w") as filer:
        json.dump(notes, filer)

def tag_add():
    tag = teg_input.text()
    note_name = Nlist.selectedItems()[0].text()
    for note in notes:
        if note["name"] == note_name:
            index = notes.index(note)
    notes[index]["tags"].append(tag)
    with open("notes.json", "w") as filer:
        json.dump(notes, filer)
    teg_list.addItem(tag)

def tag_del():
    tag = teg_list.selectedItems()[0].text()
    note_name = Nlist.selectedItems()[0].text()
    for note in notes:
        if note["name"] == note_name:
            index = notes.index(note)
    del notes[index]["tags"][notes[index]["tags"].index(tag)]
    with open("notes.json", "w") as filer:
        json.dump(notes, filer)
    teg_list.clear()
    for i in notes[index]["tags"]:
        teg_list.addItem(i)

def tag_browse():
    tag = teg_input.text()
    Nlist.clear()
    for note in notes:
        if tag in note["tags"]:
            Nlist.addItem(note["name"])
    Ntag_browse_but.setText("clear browse")
    Ntag_browse_but.clicked.disconnect()
    Ntag_browse_but.clicked.connect(browse_hide)
    
def browse_hide():
    Nlist.clear()
    for note in notes:
        Nlist.addItem(note["name"])
    Ntag_browse_but.cl.disconnect()
    Ntag_browse_but.setText("Browse notes by tags")
    Ntag_browse_but.clicked.connect(tag_browse)


for note in notes:
    Nlist.addItem(note["name"])

Nlist.itemClicked.connect(Nshow)
Ncreate_but.clicked.connect(Nadd)
Ndelete_but.clicked.connect(Ndel)
Nsave_but.clicked.connect(Nsave)
teg_add_but.clicked.connect(tag_add)
teg_delete_but.clicked.connect(tag_del)
Ntag_browse_but.clicked.connect(tag_browse)

app.exec_()# repa
