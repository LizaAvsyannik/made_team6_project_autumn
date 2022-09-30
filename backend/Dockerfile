FROM python:3.10.7-buster
RUN python -m pip install --upgrade pip
#RUN pip3 install g++
#RUN apt-get update
#RUN apt-get upgrade
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY  . .

EXPOSE 8000
EXPOSE 80
CMD ["uvicorn", "manage:app","--reload", "--host", "0.0.0.0", "--port", "8000"]