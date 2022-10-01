FROM python:3.10.7-buster
RUN python -m pip install --upgrade pip

WORKDIR /PROJECT_ROOT/backend
# install requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# install jupyter lab
RUN pip3 install jupyterlab
RUN pip install jupyterlab-code-formatter
RUN pip install black isort


#COPY  . .
#RUN rm Dockerfile
#RUN rm requirements.txt


ENV JUPYTER_ENABLE_LAB=yes
ENV JUPYTER_TOKEN=docker
EXPOSE 8000
EXPOSE 8888
EXPOSE 80

WORKDIR /PROJECT_ROOT
CMD ["bash", "backend/start.bash"]
#RUN "jupyter lab --no-browser --ip=0.0.0.0 --port=8888 &"
#CMD ["uvicorn", "manage:app","--reload", "--host", "0.0.0.0", "--port", "8000"]