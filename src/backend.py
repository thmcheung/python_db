# Feedback number
# 0 : success
# 1 : failed
# 2 : unrecognized meta command
# 3 : unrecognized sql command
# 4 : syntax error
# -1 : success quit

import os
import pickle

global PAGE_SIZE, TABLE_MAX_PAGES, ROW_SIZE
PAGE_SIZE = 4096
TABLE_MAX_PAGES = 100
ROWS_PER_PAGE = 16
TABLE_MAX_ROWS = ROWS_PER_PAGE * TABLE_MAX_PAGES

# Feedback number
# 0 : success
# 1 : failed
# 2 : unrecognized meta command
# 3 : unrecognized sql command
# 4 : syntax error
# -1 : success quit

import os
import pickle

# Constants
PAGE_SIZE = 4096
TABLE_MAX_PAGES = 100
ROWS_PER_PAGE = 16
TABLE_MAX_ROWS = ROWS_PER_PAGE * TABLE_MAX_PAGES

# Feedback numbers
SUCCESS = 0
FAILED = 1
UNRECOGNIZED_META_COMMAND = 2
UNRECOGNIZED_SQL_COMMAND = 3
SYNTAX_ERROR = 4
SUCCESS_QUIT = -1

class Row:
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"Row(id={self.id}, username='{self.username}', email='{self.email}')"

class Table:
    def __init__(self):
        self.num_rows = 0
        self.pages = [[] for _ in range(TABLE_MAX_PAGES)]
    
    def insert(self, row):
        if self.num_rows >= TABLE_MAX_ROWS:
            return FAILED
        page_num = self.num_rows // ROWS_PER_PAGE
        self.pages[page_num].append(row)
        self.num_rows += 1
        return SUCCESS

    def __repr__(self):
        return f"Table(num_rows={self.num_rows}, pages={self.pages})"

def store_feedback(feedback_number, table):
    feedback_dict = {
        SUCCESS: "success",
        FAILED: "failed",
        UNRECOGNIZED_META_COMMAND: "unrecognized meta command",
        UNRECOGNIZED_SQL_COMMAND: "unrecognized SQL command",
        SYNTAX_ERROR: "syntax error",
        SUCCESS_QUIT: "success quit"
    }
    feedback_message = feedback_dict.get(feedback_number, "unknown feedback number")
    feedback_path = 'feedback.pkl'
    
    if os.path.exists(feedback_path):
        with open(feedback_path, 'rb') as f:
            feedback_data = pickle.load(f)
    else:
        feedback_data = []

    feedback_data.append((feedback_message, table))
    
    with open(feedback_path, 'wb') as f:
        pickle.dump(feedback_data, f)
    
    return feedback_message

def save_rows_to_file(rows, filename):
    existing_rows = []
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            existing_rows = pickle.load(f)
    
    existing_rows.extend(rows)
    
    with open(filename, 'wb') as f:
        pickle.dump(existing_rows, f)
    
    print(f"Rows have been serialized and appended to {filename}")

def load_rows_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            rows = pickle.load(f)
        print(f"Rows have been loaded from {filename}")
        return rows
    else:
        print(f"No such file: {filename}")
        return []

t = Table()
r1 = Row(0, "Marcus", "gmail.com")
r2 = Row(1, "Mark", "outlook.com")
r3 = Row(1, "Mark", "yahoo.com")

feedback_number = t.insert(r1)
print(store_feedback(feedback_number, t))

feedback_number = t.insert(r2)
print(store_feedback(feedback_number, t))

feedback_number = t.insert(r3)
print(store_feedback(feedback_number, t))

rows_to_save = [r1, r2, r3]
save_rows_to_file(rows_to_save, 'rows.pkl')

loaded_rows = load_rows_from_file('rows.pkl')
print(loaded_rows)