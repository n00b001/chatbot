rm -rf _deployment
rm -rf model
rm -rf data
cd setup
python prepare_data.py
cd ../
python train.py
cd utils
python prepare_for_deployment.py
cd ..
cp app.yaml _deployment/app.yaml
cp requirements_app.txt _deployment/requirements.txt
cd _deployment
gcloud app deploy

