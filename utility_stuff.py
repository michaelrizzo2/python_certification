class shortener:
    def __init__(self,item):
        self.original_item=item

    def print_original_items(self):
        print(self.original_item)


class listandchar(shortener):
    def print_shortened_items(self):
        print(self.original_item[0:3])