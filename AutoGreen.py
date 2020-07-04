from git import Repo
import os
import sys
from datetime import datetime
import time

working_tree_dir = os.path.dirname(os.path.abspath(__file__))
stampler = os.path.abspath(str(sys.argv[1]))
repository = Repo(working_tree_dir)

def do_changes(file):
    with open(file, "a") as f:
        f.write("Greeny weeny")


def git_go_green(repo):
    repo.git.add(A=True)
    repo.git.commit('-m', "If its green, its green")
    repo.git.push('origin', 'HEAD:master')
    print('Pushed to repository')


do_changes(stampler)
git_go_green(repository)
time.sleep(4)
