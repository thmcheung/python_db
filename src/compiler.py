# 0 : success
# 1 : failed
# 2 : unrecognized meta command
# 3 : unrecognized sql command
# 4 : syntax error
# -1 : success quit
import re

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

def run_sql(statement):
    ar = re.split(r'\s+', statement.strip())
    if len(ar) < 4: 
        return 4
    if compare(ar[0], "insert"):
        #do insert
        print("delete statement detected")
        return 0
    elif compare(ar[0], "select"):
        #do select
        print("select statement detected")
        return 0
    return 3

def process(statement):
    if statement[0] == '.':
        return run_meta_statement(statement)
    else:
        return run_sql(statement)
