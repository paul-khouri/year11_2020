import os
print(os.getcwd())

def get_directory_data():
    #get current directory
    src_dir = os.getcwd()
    # go up to root folder
    #path_parent = os.path.dirname(os.getcwd())
    #dest_dir = path_parent + "/destination"
    dest_dir = src_dir
    file_list = os.listdir(dest_dir)
    #print(file_list)
    for x in file_list:
        f_path = dest_dir+"/"+x
        print(x + ": ", end="")
        print(os.stat(f_path).st_size)


get_directory_data()
