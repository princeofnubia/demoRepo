def save_in_param(param):
    file = open('param.txt', 'w')
    write = file.write(param)
    if(write > 0):
        print("File has been updated with [{0}]".format(param))
    else:
        print("Sorry an error occurred while updating the file")
    file.close()

def read_from_param():
    file = open('param.txt', 'r')
    read = file.read()
    print(read)

def file_writer(file_name = '', file_content = ''):
    if(file_name == ''):
        print("Please enter a file name")
        return
    if(file_content == ''):
        print('Please insert a content')
        return
    file = open(file_name + '.txt', 'w')
    write = file.write(file_content)
    if(write > 0):
        print("File has been updated with [{0}]".format(file_content))
    else:
        print("Sorry an error occurred while updating the file")
    file.close()

def file_writer_without_overwrite(file_name = '', file_content = ''):
    if(file_name == ''):
        print("Please enter a file name")
        return
    if(file_content == ''):
        print('Please insert a content')
        return
    file = open(file_name + '.txt', 'a')
    write = file.write(file_content)
    if(write > 0):
        print("File has been updated with [{0}]".format(file_content))
    else:
        print("Sorry an error occurred while updating the file")
    file.close()

def overwrite_or_append(file_name = '', file_content = '', write_option=True):
    if (write_option):
        file_writer(file_name, file_content)
    else:
        file_writer_without_overwrite(file_name, file_content)
def file_reader(file):
    f = open(file + '.txt', 'r')
    print('====================================')
    print('     EXAM SCORES FOR GEOGRAPHY      ')
    print('====================================')
    for i in f:
        print(i)

        

