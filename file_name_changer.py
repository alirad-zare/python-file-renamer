import os

def rename_files(path, prefix, count, files, change_order):
    renamed_count = 0
    for filename in files: 
        address_file = os.path.join(path, filename)
        file_format = os.path.splitext(filename)[1]
        new_name = f"{prefix} {count}{file_format}"
        new_file = os.path.join(path, new_name)
        if os.path.exists(new_file):
            print(f"File {new_name} already exists. Skipping renaming for {filename}.")
        else:
            os.rename(address_file, new_file)
            renamed_count += 1
            print(f"Renamed {filename} to {new_name}")   
        if change_order == "1":
            count += 1
        else:
            count -= 1
         
    return renamed_count

path = input("Enter the path of the directory: ")

if not os.path.isdir(path):
    print("Path does not exist!")
    exit()

files = []
for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            files.append(f)
fileCount = len(files)
print(f"Number of files in the directory: {fileCount}")

if fileCount == 0:
    print("No files to rename in the directory.")
    exit()

#order of files to rename

while (True):
    order = input("order of the files to rename? (alphabetical ascending (1)/alphabetical descending(2)/date created ascending(3)/date created descending(4))/date modified ascending(5)/date modified descending(6)): ").replace(" ", "")
    match order:
        case "1":
            files.sort()
            break
        case "2":
            files.sort(reverse=True)
            break
        case "3":
            files.sort(key=lambda x: os.path.getctime(os.path.join(path, x)))
            break
        case "4":
            files.sort(key=lambda x: os.path.getctime(os.path.join(path, x)), reverse=True)
            break
        case "5":
            files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
            break
        case "6":
            files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)
            break
        case _:
            print("Invalid input. Please enter a valid option.") 

prefix = input("Enter the new name for files: ")

while True:
    change_order = input("Do you want to change the order of files to rename assending (1) or descending (2)?").replace(" ", "")
    if change_order == "1" or change_order == "2":
        break
    else:
        print("Invalid input. Please enter a valid option.")

if change_order == "1":
    count = 1
    all_count = rename_files(path, prefix, count, files, change_order)
else:
    count = fileCount
    all_count = rename_files(path, prefix, count, files, change_order)
print(f"All files have been renamed successfully. {all_count} files renamed.")