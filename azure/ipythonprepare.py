import os

def installlib():
    lib_list = [
      "python-dev",
      "libxml2-dev",
      "libxslt-dev",
      "NumPy",
      "python-matplotlib",
      "python-tornado",
      "Ipython",
      "ipython-notebook",
    ]

    map(lambda x:os.system("apt-get install -y {}".format(x)),lib_list)

def install_pymodule():
    module_list = [
        "mlxtend",
        "prettyplotlib ",
        "scikit-learn",
        "Pandas",
    ]
    
    map(lambda x:os.system("pip install  {}".format(x)),module_list)  
    
def main():
  
    installlib()
    install_pymodule()


if __name__ == "__main__":
    main()
   
