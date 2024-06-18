# Feedback number
# 0 : success
# 1 : failed
# 2 : unrecognized meta command
# 3 : unrecognized sql command
# 4 : syntax error
# -1 : success quit

import os

global TABLE_MAX_PAGEs, ROW_SIZE
TABLE_MAX_PAGES = 4096
ROW_SIZE = 40

class pager:
    def __init__(self, file_descriptor: int, file_length: int, pages: list):
        self.file_descriptor = file_descriptor
        self.file_length = file_length
        self.pages = pages

class table:
    #this will be a b-tree later
    def __init__(self, num_rows, pager):
        self.num_rows = num_rows
        self.pager = []
    
    def add(self, r):
        self.num_rows += 1
        self.rows.append(r)

#returns a table that contains a pager
def db_open(filename):
    p = pager_open(filename)
    num_rows = p.file_length / ROW_SIZE
    t = table(num_rows, p)
    return table

def pager_open(filename):
    os.open(filename, os.O_RDWR | os.O_CREAT, 0o600)
    file_length = os.lseek(filename, 0, os.SEEK_END)
    pages = [None] * TABLE_MAX_PAGES
    p = pager(filename, file_length, pages)

def get_page(p:pager, page_num: int):
    if page_num > TABLE_MAX_PAGES:
        return 1
    if p.pages[page_num] == None:
        return 1
    return p.pages[page_num]
