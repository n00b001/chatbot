rm -rf _deployment
rm -rf model
rm -rf data
cd setup
python3 prepare_data.py
cd ../
python3 train.py
cd utils
python3 prepare_for_deployment.py
cd ..
cp app.yaml _deployment/app.yaml
cp requirements_app.txt _deployment/requirements.txt
cd _deployment
gcloud app deploy

