class shortener:
    def __init__(self,item):
        self.original_item=item

    def print_original_items(self):
        print(self.original_item)


class listandchar(shortener):
    def print_shortened_items(self):
        print(self.original_item[0:3])

my_shortener=listandchar("This is a test")
my_shortener.print_shortened_items()

my_shortener=listandchar([1,2,3,4,5])
my_shortener.print_shortened_items()