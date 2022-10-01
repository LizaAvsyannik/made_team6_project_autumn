#!/bin/bash



# launch jupyter lab
jupyter lab --no-browser --ip=0.0.0.0 --port=8888 --allow-root &

# download data
cd datasets
FILE=004_of_V13.csv
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gdown https://drive.google.com/uc?id=1lInIePvi6zQFyOCbsqW40w5jnUDLOfZu
fi

cd ..

#launch application
uvicorn manage:app --reload --host 0.0.0.0 --port 8000 &

# launch script to fill database
python application/main/db_utils/db_download.py

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?