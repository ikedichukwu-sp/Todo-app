import zipfile


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive(r"C:\Users\silas\PycharmProjects\pythonProject2\bonus_samples\compressed (1).zip",
                    r"C:\Users\silas\PycharmProjects\pythonProject2\bonus_samples\project_work")
