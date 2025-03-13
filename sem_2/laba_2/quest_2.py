import os
import shutil

def get_size(root_path):
    size = 0
    for root, dirs, files in os.walk(root_path):
        for file in files:
            file_path = os.path.join(root, file)
            size += os.path.getsize(file_path)
    return size
def main():
    path_to_zip = ".\\folder_with_file_and_photos.zip"
    path_to_unpacked_zip = ".\\unpacked_zip"
    shutil.unpack_archive(path_to_zip, path_to_unpacked_zip)
    result = get_size(path_to_unpacked_zip)
    print(f"Суммарный размер всех файлов: {result}")
    shutil.rmtree(path_to_unpacked_zip)
    return

if __name__ == "__main__":
    main()