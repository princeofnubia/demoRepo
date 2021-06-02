class Registry:
    def __init__(self):
        self.__TABLE_LINE = 50
        self.__HORIZONTAL_BORDER = '='
        self.__FILE_NAME = 'registry.txt'
        self.__initialize()


    def __initialize(self):
        print(self.__TABLE_LINE * self.__HORIZONTAL_BORDER)
        print('ADDEX REGISTRY')
        print(self.__TABLE_LINE * self.__HORIZONTAL_BORDER)
        self.__home()

    def __home(self):
        print('Welcome to registry type -r to register type -q to exit type -s to display the registers press -h to return home')
        self.__get_option()

    def __register(self):
        user_input = input('please enter username,number: ')
        if(self.__check(user_input)):       
            file = open(self.__FILE_NAME, 'a')
            write = file.write(user_input + '\n')
            if(write > 0):
                print("[{0}] Added to the registry".format(user_input))
            else:
                print("Sorry an error occurred while updating the file")
            file.close()
            self.__get_option()
        else:
            self.__get_option(option = user_input)

    def __check(self, user_input):
        if((user_input == '-q') or (user_input == '-r') or (user_input =='-s') or (user_input=='-h')):
            return False
        else:
            return True

    def __show(self):
        f = open(self.__FILE_NAME, 'r')
        for i in f:
            print(i)
        self.__get_option()

    def __quit(self):
        print('bye bye :)')
        return

    def __get_option(self, option=""):
        if(option == ''):
            option = input('>> ')
        # option is either a name and phonenumber, or -s, -r, -h, -q
        if(option == '-s'):
            self.__show()
        elif(option == '-r'):
            self.__register()
        elif(option == '-h'):
            self.__home()
        elif(option == '-q'):
            self.__quit()
        else:
            self.__show()

# write a feature that allows the user to empty the records