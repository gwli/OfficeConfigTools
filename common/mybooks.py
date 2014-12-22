import subprocess

books = [
    "MyLinux",
    "KnowledgeManagement",
    "Programming",
    "DeepLearningOnGPU",
]


def git_clone(book):
    print("##BEGIN:clone book:{}\n".format(book))
    subprocess.check_call(['git','clone',"http://github.com/gwli/{}.git".format(book)])
    print("##END:clone book:{}\n".format(book))
 

def main():
    map(git_clone,books)
if __name__ == "__main__":
    main()
