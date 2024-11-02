"""
1. Write a simple program
2. pip install pyinstaller
3. Generate the Executable
     Once PyInstaller is installed, navigate to the directory where greet.py is saved, then run the following command:
pyinstaller --onefile greet.py
    --onefile: This option tells PyInstaller to bundle everything into a single executable file, making it easier
    to distribute. greet.py: This is the name of the Python script you want to convert into an executable.

4. Locate the Executable
After running the command, PyInstaller will create a few directories and files. You’ll find the executable file in the
dist directory inside your project folder.

"""


def main():
    """
    Program that asks for your name and then greets you
    :return: None
    """
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to the program.")

if __name__ == "__main__":
    main()
