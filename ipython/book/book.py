import shutil
import os

def cleanup(path="."):
    ext_list = [
       "swp",
       "rst~",
    ]
    
    for root, dirs, files in os.walk(path):
        for ext_filter in ext_list:
            delete_files = filter(lambda z:z.endswith(ext_filter),files)
            print delete_files
            map(lambda x:os.remove(os.path.join(root,x)),delete_files)
       
        #delete_files= reduce(lambda x,y:filter(lambda z:z.endswith(y),x),ext_list,files)

        print delete_files


def main():
    cleanup()
if __name__ == "__main__":
    main()
