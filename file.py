import os
import shutil

# Define the path to the directory you want to organize
directory_path = "your_path"

# Define the mapping of file extensions to folder names
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"]
}

def create_folders(base_path, folders):
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder}")

def move_files_to_folders(base_path, file_mapping):
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            moved = False
            for folder, extensions in file_mapping.items():
                if file_extension in extensions:
                    dest_folder = os.path.join(base_path, folder)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    print(f"Moved {file} to {dest_folder}")
                    moved = True
                    break
            if not moved:
                dest_folder = os.path.join(base_path, "Others")
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                    print("Created folder: Others")
                shutil.move(file_path, os.path.join(dest_folder, file))
                print(f"Moved {file} to {dest_folder}")

if __name__ == "__main__":
    print("Organizing files...")
    create_folders(directory_path, file_types.keys())
    move_files_to_folders(directory_path, file_types)
    print("Files have been organized.")