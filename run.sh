#!/usr/bin/env bash
set -e
# Any subsequent(*) commands which fail will cause the shell script to exit immediately

echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Downloading data..."
rm new_data/train.from || echo ''
rm new_data/train.to || echo ''
python3 pull_data.py

echo "Removing Old Files..."
rm -rf _deployment || echo ''
rm -rf model || echo ''
rm -rf data || echo ''

echo "Preparing Data..."
cd setup
python3 prepare_data.py

echo "Training..."
cd ../
python3 train.py

echo "Preparing for Deployment..."
cd utils
python3 prepare_for_deployment.py

echo "Copying Files..."
cd ..
cp app.yaml _deployment/app.yaml
cp requirements_app.txt _deployment/requirements.txt
cd _deployment

echo "Deploying..."
gcloud app deploy -q

echo "Done!"
