#Напишите скрипт который создаст параллельно 10 файлов с именем `file_ {index}.txt'
# и записывает их номер внутрь файл

import multiprocessing

def create_file(index):
    filename = f"file_{index}.txt"
    with open(filename, "w") as file:
        file.write(str(index))

if __name__ == "__main__":
    processes = []
    for i in range(10):
        process = multiprocessing.Process(target=create_file, args=(i,))
        processes.append(process)
        process.start()


    for process in processes:
        process.join()

    print("Все файлы созданы!")