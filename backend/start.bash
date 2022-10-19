#!/bin/bash

pip3 install -r backend/requirements.txt

# download data
cd datasets


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
    gdown https://drive.google.com/file/d/1_45SwnYu5U4bvYVMKzjeG1mx4BzypZ71/view?usp=sharing

fi

cd ..


echo "Filling database with data..."
python backend/fill_db.py


# shellcheck disable=SC2164
cd backend
#launch application
uvicorn manage:app --reload --host 0.0.0.0 --port 8000 &
cd ..


# launch jupyter lab
jupyter lab --no-browser --ip=0.0.0.0 --port=8888 --allow-root &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
