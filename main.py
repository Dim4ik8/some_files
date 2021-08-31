import os

folder = 'files'

file_names = os.listdir(folder)  # []

output = 'output.txt'


def get_file_line_counts(*args):

    file_line_counts = {

    }
    for file_name in args:
        count = len(open(folder + '/' + file_name, encoding='utf-8').readlines())
        file_line_counts[file_name] = count
    return file_line_counts


def write_output_file(*files, output_filename='output.txt', folder='files'):

    line_counts = get_file_line_counts(*files)
    print('Количество строк в файлах: ', line_counts)

    line_counts_sorted = dict(sorted(line_counts.items(), key=lambda item: item[1]))

    file_names_sorted = list(line_counts_sorted.keys())
    print('Отсортированные имена файлов: ', file_names_sorted)
    for file_name in file_names_sorted:
        with open(folder + '/' + file_name, 'r', encoding='utf-8') as input_file:
            with open(output_filename, 'a', encoding='utf-8') as output_file:
                output_file.write(input_file.read())


if __name__ == '__main__':

    write_output_file(*file_names)

