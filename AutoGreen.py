from git import Repo
import os
import sys
import random


class GitGreener():

    python_version = sys.version[0]
    working_tree_dir = os.path.dirname(os.path.abspath(__file__))
    stampler = os.path.abspath(str(sys.argv[1]))
    repository = Repo(working_tree_dir)

    message = "Greeny weeny\n"

    def __init__(self):
        self.go_even_greener()


    @classmethod
    def do_changes(cls, file, message):
        with open(file, "a") as f:
            f.write(message)

    @classmethod
    def git_go_green(cls, repo):
        repo.git.add(A=True)
        repo.git.commit('-m', "If its green, its green")
        repo.git.push('origin', 'HEAD:master')
        print('Pushed to repository')

    @classmethod
    def go_even_greener(cls):

        cls.do_changes(cls.stampler, "What a green adventure!!!")
        for push in range(random.randint(2, 8)):
            cls.do_changes(cls.stampler, cls.message)
            cls.git_go_green(cls.repository)


if __name__ == '__main__':
    GitGreener()

    if GitGreener.python_version == 2:
        raw_input("Press any key to continue...")
    else:
        input("Press any key to continue...")
