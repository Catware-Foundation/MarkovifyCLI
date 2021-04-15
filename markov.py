
#
# Catware Markovify Generator
#

import markovify
import os

def readff(path):
        file = open(path, "r", encoding = "utf-8")
        contents = file.read()
        file.close()
        return contents

files_directory = input(" >>> Введите папку, из которой будут собираться файлы для чтения: ")
if files_directory.endswith("/"):
        pass
else:
        files_directory += "/"

texts = ""

for x in os.listdir(files_directory):
        try:
                content = readff(files_directory + x)
                if content not in texts:
                        texts += content + "\n"
                        print(" * Подгружен файл " + x)
        except:
                print("Не удалось подгрузить файл.")

print(" [i] Суммарный вес собранных файлов: " + str(len(content)) + " КБайт")
print(" >>> Построение модели текста...  ")
text_model = markovify.Text(texts)

print("Модель текста построена. Жмите Enter чтобы генерировать новый текст, и Ctrl-C, чтобы выйти из скрипта")
while True:
        print("=====================================================================================================")
        print(text_model.make_sentence())
        input()
