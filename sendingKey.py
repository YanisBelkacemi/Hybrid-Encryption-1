import os

def list_files_and_directories(start_path):
    # List to store found files
    found_files = []

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(start_path):
        # Print the current directory path
        print(f'Current Directory: {dirpath}')
        
        # Add files to the list
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            found_files.append(full_path)  # Add the full path of the file
            print(f'File found: {full_path}')  # Print each file found

    return found_files

# Example usage
if __name__ == "__main__":
    start_directory = '/'  # Change this to your desired starting point (e.g., 'C:\\' for Windows)
    all_files = list_files_and_directories(start_directory)

    print("\nAll files collected:")
    for file in all_files:
        print(file)
