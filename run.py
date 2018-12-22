import os
import shutil
from shutil import copyfile

import sh as sh

from setup.prepare_data import prepare
from train import train
from utils.prepare_for_deployment import prepare_deploy


def remove_old_files():
    dir = os.getcwd()
    shutil.rmtree('{}/_deployment'.format(dir), ignore_errors=True)
    shutil.rmtree('{}/model'.format(dir), ignore_errors=True)
    shutil.rmtree('{}/data'.format(dir), ignore_errors=True)


if __name__ == '__main__':
    print("Removing old files...")
    remove_old_files()

    print("Preparing dataset...")
    sh.cd("setup")
    sh.python("prepare_data.py")
    print("Training...")
    sh.cd("../")
    sh.python("train.py")

    try:
        print("Preparing to deploy...")
        prepare_deploy()
    except:
        pass

    print("Copying files...")
    sh.cp("requirements_app.txt", "_deployment/requirements.txt")
    sh.cp("app.yaml", "_deployment/app.yaml")
    sh.cd("_deployment")
    print("Deploying to google...")
    sh.gcloud.app("deploy")
    print("Done!")
