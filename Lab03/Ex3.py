import os

def find(path, filename):
    # Get all entries in the current path
    entries = os.listdir(path)

    # Iterate through each entry
    for entry in entries:
        full_path = os.path.join(path, entry)

        # If the entry is a directory, recursively call find on that directory
        if os.path.isdir(full_path):
            find(full_path, filename)

        # If the entry is a file and has the desired filename, print the full path
        elif os.path.isfile(full_path) and entry == filename:
            print(full_path)

# Example usage:
#Home pc
#find('c:/Users/Muhammad/Desktop/Comp254MS', 'Ex3.py')
#Mac
find('/Users/muhammad/Desktop', 'Ex3.py')
