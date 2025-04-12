import os
import shutil


def check_for_correct_path(path):
    if not os.path.exists(path):
        print("Такого пути не существует, попробуйте еще раз")
        return False
    if not os.path.isdir(path):
        print("Не сущестует папки с таким путем")
        return False
    return True


def transfer(src_path: str, dst_path: str):
    copies = 1
    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg"):
                file_path = os.path.join(root, file)
                if file in os.listdir(dst_path):
                    old_path = file_path
                    new_path = os.path.join(root, f"({copies})" + file)
                    os.rename(old_path, new_path)
                    file_path = new_path
                    copies += 1

                shutil.move(file_path, dst_path)


def main():
    print("Введите путь до директории с данными:")
    src_path = input()
    if not check_for_correct_path(src_path):
        return

    print("Введити путь до директории, в которую нужно перести данные: ")
    dst_path = input()
    if not check_for_correct_path(dst_path):
        return

    transfer(src_path, dst_path)
    shutil.make_archive(dst_path + "_archive", "zip", dst_path)

    return


if __name__ == "__main__":
    main()
