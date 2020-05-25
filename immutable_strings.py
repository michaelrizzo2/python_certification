my_string="abcdefg"
#When you hear of a object being immutable, this object cannot be changed.
#When you hear of an object being mutable,the objest can be changed
#==========================================
#my_string[0]=1This will result in a error sating the result cannot changed
#==========================================

my_new_string="1"+my_string[1:]
print(f"The new string is {my_new_string}")