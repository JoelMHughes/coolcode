import git

repo = Repo(repo['/users/joelhughes/projects/git_api'])
print repo.status()

def gitAdd(fileName, repoDir):
    cmd = ['git', 'add', fileName]
    p = subprocess.Popen(cmd, cwd=repoDir)
    p.wait()

gitAdd('exampleFile.txt', '/users/joelhughes/projects/git_api')
