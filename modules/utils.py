import os

FILENAME = "todotasks.txt"

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

def create_taskfile(fileName=FILENAME):
    """
    Creates a default text file if one is not provided in the argument for to-do-items
    :param filename:
    :type filename: string
    :return: file
    :rtype: str
    """
    with open(fileName, 'x') as file:
        pass
        return file

def read_taskfile(fileName=FILENAME):
    """
    Reads the text file created and returns a list of to-do-items
    :param fileName: filename
    :type fileName: string
    :return: filename
    :rtype: str
    """
    with open(fileName, 'r') as file:
        newfile = file.readlines()
    return newfile

# put the non-default parameter before default parameter (fileArg before filename)
def write_taskfile(fileArg, fileName=FILENAME):
    """
    Writes tasks to the text file
    :param fileArg: a variable set for the file list
    :type fileArg: str
    :param fileName: default filename to write to. Can be changed to by explicitly typing another name
    :type fileName: str
    :return: none
    :rtype: none
    """
    with open(fileName, 'w+') as file:
        file.writelines(fileArg)

def delete_taskfile(fileName=FILENAME):
    """
    Deletes task file from the system
    :param fileName: name of file to be deleted
    :type fileName: str
    :return: None
    :rtype: None
    """
    if os.path.isfile(fileName):
        os.remove(fileName)
        print(f"File {fileName} deleted.")
    else:
        print(f"Error: File {fileName} not found.")

if __name__ == "__main__":
    print("Executing the functions")