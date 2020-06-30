class shortener:
    def __init__(self,item):
        self.original_item=item

    def print_original_items(self):
        print(self.original_item)


class listandchar(shortener):
    def print_shortened_items(self):
        print(self.original_item[0:3])

class dict_shortener(shortener):
    def print_shortened_items(self):
        my_dict=self.original_item
        for index in list(my_dict.keys())[3:]:
            my_dict.pop(index)
        print(my_dict)
my_shortener=listandchar("This is a test")
my_shortener.print_shortened_items()
my_shortener.print_original_items()

my_shortener=listandchar([1,2,3,4,5])
my_shortener.print_shortened_items()
my_shortener.print_original_items()

my_shortener=dict_shortener({"1":1,"2":2,"3":3,"4":4})
my_shortener.print_shortened_items()