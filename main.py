# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться
import pytest
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def people(numbers):
    for document_number in documents:
        if document_number["number"] == numbers:
            return (document_number["name"])
            #break
    else:
        print("Введен несуществующий номер документа.")

def shelf(numbers):
    break_marker = False
    for shelf_directories in directories.items():
        for document_number in shelf_directories[1]:
            if document_number == numbers:
                return shelf_directories[0]
                #break_marker = True
                #break
        if break_marker == True:
          break
    else:
        print("Введен несуществующий номер документа.")

def people_list():
    for people in documents:
        print(people["type"], '"' + people["number"] + '"', '"' + people["name"] + '"')

def add_command(params_type, number, name, directories_number):
    if int(directories_number) == 1 or int(directories_number) == 2 or int(directories_number) == 3:
        documents.append({"type": params_type, "number": number, "name": name})
        directories[directories_number].append(number)
    else:
        return "Введенной полки не существует"

# while True:
#     command = input("Введите одну из команд: p, s, l, a: \n  ")
#     if command == "p":
#         people(input("Введите номер документа:"))
#     elif command == "s":
#         shelf(input("Введите номер документа:"))
#     elif command == "l":
#         people_list()
#     elif command == "a":
#         add_command(input("Введите тип документа:"), input("Введите номер документа:"), input("Введите имя:"),
#                     input("Введите номер полки (1, 2, 3):"))
#         print(documents)
#         print(directories)
#     else:
#         print("Вы ввели некорректную команду, повторите ввод.")