# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True,
# если команда успешно выполнена и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.


import subprocess

def execute_command_and_find_text(command, text):
    # Выполняем команду
    output = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Проверяем, успешно ли выполнена команда и ищем текст в выводе
    if output.returncode == 0 and text in output.stdout:
        return True
    else:
        return False


command = "ls -l"
text = "file.txt"

result = execute_command_and_find_text(command, text)
print(result)