class row:
    #this will not be hardcoded in the final product
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

class table:
    #this will be a b-tree later
    def __init__(self):
        self.num_rows = 0
        self.rows = []
    
    def add(self, r):
        self.num_rows += 1
        self.rows.append(r)