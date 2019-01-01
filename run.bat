cd setup
python36 prepare_data.py

cd ../
python36 train.py

cd utils
python36 prepare_for_deployment.py

pause
