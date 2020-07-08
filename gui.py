# -*- coding: utf-8 -*-
from guizero import App, Text, TextBox, PushButton
import os
import json
from shutil import copyfile


def _get_comment_from_json(filename):
    with open(path_to_json_directory+"\\"+filename, 'r', encoding='UTF-8') as f:
        return json.load(f)["komentarz"]


path_to_json_directory = "C:\\Users\\mackow\\PycharmProjects\\mgr\\komentarze\\json_files"
path_to_comments = "C:\\Users\\mackow\\PycharmProjects\\mgr\\komentarze\\rodzaje_komentarzy"


files = os.listdir(path_to_json_directory)
files.sort(key= lambda x: int(x.split(".")[0]))
print(files)
iter = (file.split(".")[0] for file in files)
actual_gen_value = next(iter)
first_comment = _get_comment_from_json(actual_gen_value+".json")
app = App(title="Klasyfikacja komentarzy", bg='#e6ffff', layout='grid', height=480, width=570)

intro = TextBox(app, text=first_comment, multiline=True, align='top', width=70, height=20, grid=[2, 1, 5, 1])
text2 = Text(app, text=actual_gen_value, grid=[2, 2, 5, 2])


def info(txt):
    try:
        new_value = int(next(iter))
        old_value = new_value - 1
        copyfile(path_to_json_directory + "\\" + str(old_value) + ".json",
                 path_to_comments + '\\' + txt + '\\' + str(old_value)+".json")
        os.remove(path_to_json_directory + "\\" + str(old_value) + ".json")
        intro.value = _get_comment_from_json(str(new_value)+".json")
        text2.value = str(int(text2.value) + 1)

    except StopIteration:
        last = actual_gen_value
        copyfile(path_to_json_directory + "\\" + str(last) + ".json",
                 path_to_comments + '\\' + txt + '\\' + str(last)+".json")
        os.remove(path_to_json_directory + "\\" + str(last) + ".json")
        app.destroy()


p0 = PushButton(app, text="USUŃ", grid=[2, 2], padx=5, width=5, command=info, args=("usuniete",))
p1 = PushButton(app, text="Groźby karalne", grid=[3, 5], padx=20, width=10, command=info, args=("grozby_karalne",))
p2 = PushButton(app, text="Obraźliwe", grid=[4, 5], padx=20, width=10, command=info, args=("obrazliwe",))
p3 = PushButton(app, text="Złośliwe", grid=[5, 5], padx=20, width=10, command=info, args=('zlosliwe',))
p4 = PushButton(app, text="Ostra Krytyka", grid=[3, 6], padx=20, width=10, command=info, args=("ostra_krytyka",))
p5 = PushButton(app, text="Krytyka", grid=[4, 6], padx=20, width=10, command=info, args=("krytyka",))
p6 = PushButton(app, text="Dopuszczalne", grid=[5, 6], padx=20, width=10, command=info, args=('dopuszczalne',))


def del_fol():
    files_to_delete = os.listdir(path_to_comments)
    for folder in files_to_delete:
        for file in os.listdir(path_to_comments+"\\"+folder):
            os.remove(path_to_comments + "\\" + folder + "\\" + file)


# del_fol()       # SETUP: czyszczenie folderów
app.display()
