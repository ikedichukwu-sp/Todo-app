import pathlib
import zipfile


def make_archive(filepaths, desk_dir):
    # Create the full path for the zip file (compressed.zip inside the desk_dir)
    desk_path = pathlib.Path(desk_dir, "compressed.zip")

    # Open the zip file using desk_path
    with zipfile.ZipFile(desk_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_archive(filepaths=["gui.py", "feet_inches.py"], desk_dir="bonus_samples")
