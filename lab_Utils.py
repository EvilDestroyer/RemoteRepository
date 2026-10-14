# Функция для чтения текста из файла
def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Функция для записи текста в файл
def write_text(path, content="No text was supplied"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Функция для подсчёта количества строк в файле
def count_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)