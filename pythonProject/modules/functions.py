path = "Files/todos.txt"

def get_todos(filepath=path):
    """
    Read a file and return the list of to-do items
    :param filepath:
    :return:  list
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = path ):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    #Il valore di __name__ è main solo se si esegue il codice del modulo. se il modulo viene richiamato il valore sarà il nome del modulo
    print("Hello")