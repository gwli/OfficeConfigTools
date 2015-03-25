import os

def installlib():
    lib_list = [
      "libatlas-base-dev", 
      "python-dev", "python-nose",
      "libxml2-dev",
      "libxslt-dev",
      "NumPy",
      "python-scipy",
      "python-matplotlib",
      "python-tornado",
      "Ipython",
      "ipython-notebook",
      "python-opencv",
    ]

    map(lambda x:os.system("apt-get install -y {}".format(x)),lib_list)

def install_pymodule():
    module_list = [
        "mlxtend",
        #"sciPy",
        "prettyplotlib ",
        "scikit-learn",
        "Pandas",
	"FLANN",
=======
        "gitpython",
        #"nbdiff",
        "Theano",
        #"NbConvert",
>>>>>>> 9e368b16ce0643125e25acda943728d63d8cee2c
    ]
    
    map(lambda x:os.system("pip install  {}".format(x)),module_list)  
    
def main():
  
    installlib()
    install_pymodule()


if __name__ == "__main__":
    main()
   
