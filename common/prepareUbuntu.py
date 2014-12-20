import subprocess 
libs = [
  "ipython"
  "vim"
  "build-essential"
  "apt-file"
]


def install(package):
    print("##Begin install package:{} \n".fomrat(package))
    subprocess.check_call(['apt-get','-y','install',package])
    print("##End install package:{} \n".fomrat(package))


def main():
    map(install,libs)

if __name__== "__main__":
     main()
