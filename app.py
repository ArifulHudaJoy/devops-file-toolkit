#!/usr/bin/env python3
"""
DevOps File Toolkit (Student Project)
Author: ArifulHudaJoy

A practical Python CLI tool demonstrating real skills:
- File creation, reading, writing, appending
- Search & replace inside files
- Safe delete
- Folder operations
- Copy / move files & directories
- Path handling + safety checks

Built using: Python, os, shutil
Purpose: Academic portfolio (Bachelor admission + GitHub)
"""

import os
import shutil


def create_file(path):
    content = input("Enter initial content: ")
    with open(path, "w") as f:
        f.write(content + "\n")
    print("File created successfully.")


def read_file(path):
    if os.path.isfile(path):
        with open(path, "r") as f:
            print("\n--- File Content ---")
            print(f.read())
    else:
        print("File does not exist.")


def append_file(path):
    if os.path.isfile(path):
        content = input("Enter content to append: ")
        with open(path, "a") as f:
            f.write(content + "\n")
        print("Content appended.")
    else:
        print("File does not exist.")


def search_word(path):
    if os.path.isfile(path):
        word = input("Word to search: ")
        found = False
        with open(path, "r") as f:
            for line_no, line in enumerate(f, start=1):
                if word in line:
                    print(f"Found at line {line_no}: {line.strip()}")
                    found = True
        if not found:
            print("Word not found.")
    else:
        print("File does not exist.")


def replace_word(path):
    if os.path.isfile(path):
        old = input("Word to replace: ")
        new = input("Replace with: ")
        with open(path, "r") as f:
            content = f.read()
        content = content.replace(old, new)
        with open(path, "w") as f:
            f.write(content)
        print("Replacement complete.")
    else:
        print("File does not exist.")


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print("File deleted.")
    else:
        print("File not found.")


def create_folder(path):
    os.makedirs(path, exist_ok=True)
    print("Folder created.")


def delete_folder(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("Folder deleted.")
    else:
        print("Folder not found.")


def copy_item(src, dest):
    if os.path.isfile(src):
        shutil.copy(src, dest)
    elif os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        print("Source not found.")
        return
    print("Copy completed.")


def move_item(src, dest):
    if os.path.exists(src):
        shutil.move(src, dest)
        print("Move completed.")
    else:
        print("Source not found.")


def menu():
    while True:
        print("""
DevOps File Toolkit
1. Create file
2. Read file
3. Append file
4. Search word
5. Replace word
6. Delete file
7. Create folder
8. Delete folder
9. Copy file/folder
10. Move file/folder
11. Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            create_file(input("File path: "))
        elif choice == "2":
            read_file(input("File path: "))
        elif choice == "3":
            append_file(input("File path: "))
        elif choice == "4":
            search_word(input("File path: "))
        elif choice == "5":
            replace_word(input("File path: "))
        elif choice == "6":
            delete_file(input("File path: "))
        elif choice == "7":
            create_folder(input("Folder path: "))
        elif choice == "8":
            delete_folder(input("Folder path: "))
        elif choice == "9":
            src = input("Source path: ")
            dest = input("Destination path: ")
            copy_item(src, dest)
        elif choice == "10":
            src = input("Source path: ")
            dest = input("Destination path: ")
            move_item(src, dest)
        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
