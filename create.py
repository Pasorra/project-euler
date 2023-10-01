import sys
import subprocess
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create.py <filename>")
    else:
        filename = sys.argv[1]

        if not filename:
            print("Usage: python create.py <filename>")
            exit(1)

        # Replace spaces with underscores in the filename
        filename = filename.replace(" ", "_")

        # Create the Python file
        with open(f"{filename}.py", "w"):
            pass

        print(f"Created {filename}.py in the current directory.")
        print(os.path.abspath(__file__))
        path = os.path.abspath(__file__).split("\\")
        path[-1] = filename + ".py"
        path ="\\".join(path) 
        print(path)
        print(os.path.isfile(path))
        # Open the file in VSCode
        subprocess.run(f'code "{path}"', shell=True)

