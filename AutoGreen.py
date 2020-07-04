from git import Repo
import os
import sys
from datetime import datetime


working_tree_dir = os.path.dirname(os.path.abspath(__file__))
stampler = os.path.abspath(str(sys.argv[1]))
repository = Repo(working_tree_dir)

def do_changes(file):
    with open(file, "a") as f:
        f.write(f"Date and time: {datetime.now().strftime('%H:%M:%S, %m/%d/%Y')}\n")

def git_go_green(repo):
    if len(repo.untracked_files):
        repo.git.add(A=True)
        repo.git.commit('-m', f"Date and time: {datetime.now().strftime('%H:%M:%S, %m/%d/%Y')}")
        repo.git.push('origin', 'HEAD:refs/for/master')

do_changes(stampler)
git_go_green(repository)