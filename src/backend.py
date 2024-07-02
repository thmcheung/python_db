# Feedback number
# 0 : success
# 1 : failed
# 2 : unrecognized meta command
# 3 : unrecognized sql command
# 4 : syntax error
# -1 : success quit

import os

global PAGE_SIZE, TABLE_MAX_PAGES, ROW_SIZE
PAGE_SIZE = 4096
TABLE_MAX_PAGES = 100
ROW_SIZE = 256


class Pager:
    def __init__(self, file_descriptor: int, file_length: int):
        self.file_descriptor = file_descriptor
        self.file_length = file_length
        self.pages = [None] * TABLE_MAX_PAGES

class Table:
    def __init__(self, num_rows, pager):
        self.num_rows = num_rows
        self.pager = pager
    
    def add(self, r):
        self.num_rows += 1
        self.pager.append(r)

#returns a table that contains a pager
def db_open(filename):
    p = pager_open(filename)
    num_rows = p.file_length / ROW_SIZE
    t = Table(num_rows, p)
    return Table

def pager_open(filename):
    with open(filename, 'a+b') as f:  #Open the file in append + binary mode
        fd = f.fileno()  #Get the file descriptor
        f.seek(0, os.SEEK_END)
        file_length = f.tell()
    p = Pager(fd, file_length)
    return p

def get_page(pager:Pager, page_num):
    if page_num > TABLE_MAX_PAGES:
        return 1
    if pager.pages[page_num] == None:
        #none in memory, have to go in file
        num_pages = pager.file_length / PAGE_SIZE
        if pager.file_length % PAGE_SIZE != 0:
            num_pages += 1
    if page_num <= num_pages:
        os.lseek(pager.file_descriptor, page_num * PAGE_SIZE, os.SEEK_SET)
        bytes_read = os.read(pager.file_descriptor, PAGE_SIZE)
        if bytes_read == -1:
            return 1
        else:
            pager.pages[page_num] = bytes_read
            return pager.pages[page_num]
