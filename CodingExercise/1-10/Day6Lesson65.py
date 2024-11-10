
while True:
    user_input = input("Enter add, show or exit: ")

    match(user_input):
        case'add':

            user_input = input("Enter person name: ")

            file = open("Files/members.txt", 'r')
            names = file.readlines()
            file.close()

            names.append(user_input)

            file = open('Files/members.txt', 'w')
            file.writelines(names)
            file.close()

        case 'show':

            file = open("Files/members.txt", 'r')
            names = file.readlines()
            file.close()

            for n in names:
                print(n)
        case 'exit':
            break

