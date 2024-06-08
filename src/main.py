# Feedback number
# 0 : success
# 1 : failed
# 2 : unrecognized meta command
# 3 : unrecognized sql command
# -1 : success quit
import compiler

if __name__ == '__main__':
    while True:
        statement = input("db > ")
        feedback = compiler.process(statement)
        if feedback == 0:
            print("success")
            #not implemented yet
        elif feedback == 1:
            print("failure")
        elif feedback == 2:
            print("unrecognized meta command")
        elif feedback == 3:
            print("unrecognized sql command")
        elif feedback == -1:
            print("exit successful")
            break
    exit()