import os

def print_directory_contents(path):
    try:
        # Get the list of all files and directories in the specified path
        entries = os.listdir(path)
        
        print(f"Contents of '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path
directory_path = '.'  # Current directory, change this to any directory path you want

print_directory_contents(directory_path)
