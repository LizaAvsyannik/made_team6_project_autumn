#!/bin/bash

pip3 install -r backend/requirements.txt

# download data
cd datasets

pip3 install --upgrade gdown

FILE=004_of_V13.csv
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/uc?id=1lInIePvi6zQFyOCbsqW40w5jnUDLOfZu
fi


FILE=topics.json
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/u/0/uc?id=1_45SwnYu5U4bvYVMKzjeG1mx4BzypZ71

fi

cd ..


echo "Filling database with data..."
python backend/fill_db.py


# shellcheck disable=SC2164
cd backend


cd source_for_models

FILE=author.index
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/u/0/uc?id=1jcg27-SidC_ojD1pGkTMubdNl3V1e4hP

fi

FILE=paper.index
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/u/0/uc?id=1cgnbcaL9LyT2IXNKsPvqT5JZal8E84lO

fi

FILE=authors.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/u/0/uc?id=15_uz4Xsg9ACtAk2NO6DBRjB7bRC_Ig5l

fi

FILE=papers.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/u/0/uc?id=1fkFZN2OimnPZzz54dXkLDteOcmhBbKOL

fi

FILE=author2idx.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    wget https://raw.githubusercontent.com/LizaAvsyannik/made_team6_project_autumn/recsys/recsys/data/author2idx.pkl

fi

FILE=idx2author.pkl
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    wget https://raw.githubusercontent.com/LizaAvsyannik/made_team6_project_autumn/recsys/recsys/data/idx2author.pkl

fi

cd ..

#launch application
uvicorn manage:app --reload --host 0.0.0.0 --port 8000 &
cd ..


# launch jupyter lab
jupyter lab --no-browser --ip=0.0.0.0 --port=8888 --allow-root &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
