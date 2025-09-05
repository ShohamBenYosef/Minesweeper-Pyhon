class Cell(object):
    def __init__(self):
        self.is_mine = False
        self.is_visible = False
        self.is_flag = False
        self.neighbor_mines = 0


    def reveal(self):
        self.is_visible = True

    #
    def toggle_flag(self):
        self.is_flag = not self.is_flag

