FROM python:3.6.9-alpine3.10

COPY requirements.txt ./requirements.txt
COPY scrapeandrest.py ./scrapeandrest.py
COPY data.json ./data.json

# Environment Varaibles
ENV DISPLAY=:10



RUN pip install --upgrade setuptools
RUN pip3 install --requirement /requirements.txt

# install geckodriver and firefox
RUN wget https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/45.0.2/linux-x86_64/en-US/firefox-45.0.2.tar.bz2
RUN tar -xjvf firefox*.tar.bz2
RUN mv firefox /opt/firefox
RUN ln -sf /opt/firefox/firefox /usr/bin/firefox



WORKDIR /code
ADD requirements.txt /code
ADD scrapeandrest.py /code
ADD geckodriver.log /.local/bin 



CMD [ "python", "./scrapeandrest.py" ]
