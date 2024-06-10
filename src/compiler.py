# 0 : success
# 1 : failed
# 2 : unrecognized meta command
# 3 : unrecognized sql command
# 4 : syntax error
# -1 : success quit
import re
import backend

def compare(a, b):
    #Compares lower case
    #True if a == b
    #False otherwise
    if a.lower() == b.lower():
        return True
    else:
        return False

def run_meta_statement(statement):
    match statement:
        case ".exit":
            return -1 #exit statement
        case _:
            return 2 #unrecognized meta command

def execute(statement, table):
    ar = re.split(r'\s+', statement.strip())
    if compare(ar[0], "insert"):
        if len(ar) < 4:
            return 4
        else:
            r = backend.row(ar[1], ar[2], ar[3])
            table.add(r)
            return 0
    elif compare(ar[0], "select"):
        for r in table.rows:
            print(r.id, r.username, r.email)
        return 0
    return 3

def process(statement, table):
    if statement[0] == '.':
        return run_meta_statement(statement)
    else:
        return execute(statement, table)
