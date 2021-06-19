import random
import uuid
import os

# this is pet project. I learn python since 17 jun 2021. i want learn neuron


class ManagePassWrapper:

    def generate_pass_(self):
        print("Сколько вам необходимо паролей?")
        numPass = int(input())
        i = 0
        while i < numPass:
            safeId = uuid.uuid4()
            print(safeId)
            i = i + 1

    def save_new_pass_(self):
        file = open('pass.kblt', 'a')

        print("Вводите пароли, которые необходимо сохранть, по завершении введите null")
        saveThis = input()
        while saveThis != 'null':
            file.write(saveThis + "\n")
            saveThis = input()
        file.close()

    def delete_file(self):
       os.remove('pass.kblt')

       print("Файл удалён успешно")

    def read_pass_in_file(self):
        file = open('pass.kblt', 'r')
        text = file.read()
        print(text)
        file.close()

obj = ManagePassWrapper()
print('Введите команду: 0 - генерация паролей, 1 - запись в файл паролей, 2 - удалить пароли, 3 - прочесть пароли')
command = int(input())
if command == 0:
    obj.generate_pass_()
elif command == 1:
    obj.save_new_pass_()
elif command == 2:
    obj.delete_file()
elif command == 3:
    obj.read_pass_in_file()
else:
    print('Вероятно вы ошиблись командой')



