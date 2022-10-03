#!/bin/bash

# download data
cd datasets


FILE=004_of_V13.csv
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/uc?id=1lInIePvi6zQFyOCbsqW40w5jnUDLOfZu
fi

FILE=random_10k_from_first_200k.json
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/uc?id=1f3F0iG3sxpNG0Gu5ISj561H4nVifGVan

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
