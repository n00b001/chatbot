#!/usr/bin/env bash
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Downloading data..."
export GOOGLE_APPLICATION_CREDENTIALS="g_credentials.json"
python3 pull_data.py

echo "Removing Old Files..."
rm -rf _deployment
rm -rf model
rm -rf data

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
gcloud app deploy

echo "Done!"
