FROM python:3.12.4

# upgrade pip
RUN pip install --upgrade pip

# permissions and nonroot user for tightened security
RUN useradd -m nonroot
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /home/app
USER nonroot

# copy all the files to the container
COPY --chown=nonroot:nonroot . .

# venv
ENV VIRTUAL_ENV=/home/app/venv

# python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt

# install fasttext
RUN git clone https://github.com/facebookresearch/fastText.git
RUN cd fastText && pip install .

# define the port number the container should expose
EXPOSE 8000

CMD ["python", "app.py"]
