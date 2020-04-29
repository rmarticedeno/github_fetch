
#!/usr/bin/python3
import git
import os
from config import repo_path, after_pull_instructions

repo = git.Repo( repo_path if repo_path != '' else os.getcwd())

def get_latest_remote_commit(repo):
    return repo.git.ls_remote("--heads", "origin", 'gh-pages').split()[0]

def get_latest_local_commit(repo):
    return repo.commit('gh-pages')

if get_latest_local_commit(repo) != get_latest_remote_commit(repo):
    git = repo.git
    repo.heads.default.checkout()
    git.pull('origin', 'default')
    git.branch('-d','gh-pages')
    git.checkout('-b', 'gh-pages')
    git.pull('origin', 'gh-pages')
    if after_pull_instructions:
        fd = open(after_pull_instructions, 'r')
        instructions = fd.readlines()
        for ins in instructions:
            os.system(ins)