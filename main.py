import os

# Папка с обрабатываемыми файлами
folder = 'files'

# Список файлов из папки
file_names = os.listdir(folder)  # []

# Выходной файл
output = 'output.txt'


def get_file_line_counts(*args):
    """
    Функция, получающая количество строк в каждом файле
    :param args: Названия файлов(list or tuple)
    :return: Словарь вида: {'2.txt': 1, '1.txt': 2}
    """
    file_line_counts = {
        # 'file_name': 'number of strings'
    }
    for file_name in args:
        count = len(open(folder + '/' + file_name, encoding='utf-8').readlines())
        file_line_counts[file_name] = count
    return file_line_counts


def write_output_file(*files, output_filename='output.txt', folder='files'):
    """
    Функция собирает файлы из папки, сортирует по количеству строк и записывает в новый файл
    :param files: Названия файлов(list or tuple)
    :param output_filename: Название или путь к выходному файлу
    :param folder: Папка из которой берутся исходные файлы
    :return: None
    """

    # Считаем количество строк в файлах
    line_counts = get_file_line_counts(*files)
    print('Количество строк в файлах: ', line_counts)

    # Сортируем файлы по количеству строк
    line_counts_sorted = dict(sorted(line_counts.items(), key=lambda item: item[1]))

    # Извлекем имена файлов в правильном порядке
    file_names_sorted = list(line_counts_sorted.keys())
    print('Отсортированные имена файлов: ', file_names_sorted)
    for file_name in file_names_sorted:
        # Считываем каждый файл и записываем его в выходной файле
        with open(folder + '/' + file_name, 'r', encoding='utf-8') as input_file:
            with open(output_filename, 'a', encoding='utf-8') as output_file:
                output_file.write(input_file.read())


if __name__ == '__main__':

    write_output_file(*file_names)
    # print(get_file_line_counts(*file_names))
