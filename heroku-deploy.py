import os
import shutil
import sys

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

def init_deploy():
    shutil.rmtree(os.path.join(FILE_PATH, 'web'), ignore_errors=True)

def build_backend():
    os.system('(cd packages/back && yarn && yarn build:heroku)')

def copy_backend():
    shutil.rmtree(os.path.join(FILE_PATH, 'packages', 'back', 'build'), ignore_errors=True)
    shutil.copytree(
        os.path.join(FILE_PATH, 'packages', 'back'),
        os.path.join(FILE_PATH, 'web'),
        ignore=shutil.ignore_patterns('node_modules', 'src', 'babel.config.js', '.prettierrc.js', '.gitignore', 'tests'))
    shutil.rmtree(os.path.join(FILE_PATH, 'packages', 'back', 'back'))

def build_frontend():
    os.system('yarn build:front')

def copy_frontend():
    shutil.copytree(
        os.path.join(FILE_PATH, 'packages', 'front', 'build'),
        os.path.join(FILE_PATH, 'web', 'front', 'build'))
    shutil.rmtree(os.path.join(FILE_PATH, 'packages', 'front', 'build'))

def push_to_heroku():
    os.system('git add .')
    os.system('git commit -m "Commit from heroku-deploy.py for deployment"')
    os.system('git push origin master')
    os.system('git subtree push --prefix web heroku master')

def main():
    init_deploy()
    build_backend()
    copy_backend()
    build_frontend()
    copy_frontend()
    push_to_heroku()

if __name__ == "__main__":
    main()

