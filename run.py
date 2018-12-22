from shutil import copyfile

import sh as sh

from setup.prepare_data import prepare
from train import train
from utils.prepare_for_deployment import prepare_deploy

if __name__ == '__main__':
    prepare()
    train()
    prepare_deploy()
    copyfile("requirements_app.txt", "_deployment/requirements.txt")
    copyfile("app.yaml", "_deployment/app.yaml")
    sh.cd("_deployment")
    print("Deploying to google...")
    sh.gcloud.app("deploy")
