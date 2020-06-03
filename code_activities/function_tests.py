

my_string = "hello"

def test_function():
    global my_string
    my_string = "bob"

test_function()
print(my_string)
    
