import compiler

if __name__ == '__main__':
    while True:
        statement = input("db > ")
        if statement[:5].lower() == ".exit":
            break
        else:
            print("unrecognized")
            #add this to compiler
    exit()