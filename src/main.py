# Feedback number
# 0 : success
# 1 : failed
# 2 : unrecognized meta command
# 3 : unrecognized sql command
# 4 : syntax error
# -1 : success quit
import compiler
import backend

if __name__ == '__main__':
    t = backend.db_open()
    while True:
        statement = input("db > ")
        feedback = compiler.process(statement, t)
        if feedback == 1:
            print("failure")
        elif feedback == 2:
            print("unrecognized meta command", statement)
        elif feedback == 3:
            print("unrecognized sql command")
        elif feedback == 4:
            print("syntax error")
        elif feedback == -1:
            print("exit successful")
            break
    exit()