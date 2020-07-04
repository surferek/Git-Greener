from git import Repo
import os
import sys
from datetime import datetime


working_tree_dir = os.path.dirname(os.path.abspath(__file__))
stampler = os.path.abspath(str(sys.argv[1]))
repository = Repo(working_tree_dir)

def do_changes(file):
    with open(file, "a") as f:
        f.write("Date and time: {}\n".format(datetime.now().strftime('%H:%M:%S, %m/%d/%Y')))


def git_go_green(repo):
    repo.git.add(A=True)
    repo.git.commit('-m', "Date and time: {}".format(datetime.now().strftime('%H:%M:%S, %m/%d/%Y')))
    repo.git.push('origin', 'HEAD:master')
    print('Pushed')


do_changes(stampler)
git_go_green(repository)

