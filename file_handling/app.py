import os


def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"file name {filename}: created")

    except FileExistsError:
        print(f"file name{filename}: already exist")

    except Exception as E:
        print("An error occured")

def view_file():
    file = os.listdir()
    if not file:
        print("no file found")
    else:
        print("files in Directory")
        for i in file:
            print(i)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename}: not found")

    except Exception as E:
        print("An error occured")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"contect of {filename} : \n{content}")

    except FileExistsError:
        print(f"{filename} not found")

    except Exception as E:
        print("An error occured")

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content = input("Enter data to add: ")
            f.write(content + '\n')
            print(f'content add to {filename} Success')
    except FileExistsError:
        print(f"{filename} not found")

    except Exception as E:
        print("An error occured") 
def save_file(filename,directory,content):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory,filename)
        with open(filename,'w') as f:
            f.write(content)
        print(f"file {filename} successfully in directory{directory}")

    except FileExistsError:
        print(f"{filename} file deleted")

    except Exception as E:
        print("An error occured") 

def main():
    while True:
        print("FILE MANAGEMENT APPLICATION")
        print('1: create file')
        print('2: view all file') 
        print('3: delete file') 
        print('4: read file') 
        print('5: edit file')
        print('6: save file')
        print('7: exit')

        choice = input("Enter your choice(1-7)= ")

        if choice == '1':
            filename = input("Enter file name to create: ")
            create_file(filename)
        elif choice =='2':
            view_file()
        elif choice =='3':
            filename = input("Enter name of your file: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter name to read: ")
            read_file(filename=filename)
        elif choice == '5':
            filename = input("Enter file name to exit: ")
            edit_file(filename)
        elif choice == '6':
            filename = input("Enter the file name to save: ")
            directory = input("Enter the directory to save the file: ")
            content = input("Enter the content to save: ")
            save_file(filename, directory, content)
        elif choice == '7':
            print("Closing the app")
            break
        else:
            print("Enter the valid input")            

if __name__ =='__main__':
    main()


