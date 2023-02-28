
#
# Catware Markovify Generator
#

import os

import markovify


def readff(path):
    with open(path, encoding="utf-8") as file:
        return file.read()


files_directory = input(" >>> Введите папку, из которой будут собираться файлы для чтения: ")
if not files_directory.endswith("/"):
    files_directory += "/"

texts = ""

for x in os.listdir(files_directory):
    try:
        content = readff(files_directory + x)
        if content not in texts:
            texts += content + "\n"
            print(" * Подгружен файл " + x)
    except Exception as e:
        print(f"Не удалось подгрузить файл (ошибка {e}).")

print(f" [i] Суммарный вес собранных файлов: {len(content)} КБайт")
print(" >>> Построение модели текста...  ")
text_model = markovify.Text(texts)

print("Модель текста построена. Жмите Enter чтобы генерировать новый текст, и Ctrl-C, чтобы выйти из скрипта")
while True:
    print('=' * 101)
    print(text_model.make_sentence())
    input()
