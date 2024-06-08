def run_meta_statement(statement):
    match statement:
        case ".exit":
            return -1 #exit statement
        case _:
            return 2 #unrecognized meta command

def run_sql(statement):
    # needs to be tokenized and parsed
    return 3


def process(statement):
    if statement[0] == '.':
        return run_meta_statement(statement)
    else:
        return run_sql(statement)