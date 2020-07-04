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


def get_status(repo, path):
    changed = [ item.a_path for item in repo.index.diff(None) ]
    if path in repo.untracked_files:
        return 'Untracked'
    elif path in changed:
        return 'Modified'
    else:
        return 'Doesen\'t matter'

print(get_status(repository, working_tree_dir))

def git_go_green(repo):
    repo.git.add(A=True)
    repo.git.commit('-m', f"Date and time: {datetime.now().strftime('%H:%M:%S, %m/%d/%Y')}")
    repo.git.push('origin', 'HEAD:master')
    print('Pushed')


do_changes(stampler)
git_go_green(repository)