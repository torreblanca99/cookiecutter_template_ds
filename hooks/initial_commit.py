import os
import sys
import shutil

branch_name = 'develop'

FILES_COPY = [
    'models/*',
    'notebooks/*',
    '{{cookiecutter.module_name}}/*',
    '.gitignore',
    'LICENSE',
    'README.md',
    'poetry.lock'
    'pyproject.toml',
    '.pre-commit-config.yaml',
    ]

repo_name = '{{cookiecutter.repo_name}}'

def generate_new_branch():s
    """
    Creates a new Git branch with the name specified in the `branch_name` variable.
    If the branch creation fails, the script exits with an error message.
    """

    if os.system(f'git checkout -b {branch_name}') != 0:
        sys.exit(f"""Brack {branch_name} could not be created""")

def move_and_override_elements():
    """
    Copies files and directories specified in the `FILES_COPY` list from the repository
    to the parent directory. If the file pattern contains a wildcard '*', it creates the
    necessary directories and copies the matching files.
    """

    print('Moving files')
    for f in FILES_COPY:
        source = os.path.join(repo_name, f)
        if '*' not in f:
            os.system(f'cp -r {source} ../{f}')
        else:
            os.makedirs(f'../{f[:-1]}', exist_ok=True)
            os.system(f'cp -r {source} ../{f[:-1]}')


if __name__ == '__main__':
    #generate_new_branch()
    move_and_override_elements()
