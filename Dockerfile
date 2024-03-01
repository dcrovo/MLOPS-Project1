FROM tensorflow/tfx:latest
RUN mkdir /data 
RUN mkdir /work
WORKDIR /work
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install jupyter==1.0.0 -U && pip install jupyterlab==3.6.1
EXPOSE 8888
ENTRYPOINT [ "jupyter", "lab","--ip=0.0.0.0", "--alow-root" ]