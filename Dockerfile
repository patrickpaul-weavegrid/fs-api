FROM python:3.12
RUN mkdir /var/code; \
    cd /var/code; \
    git clone https://github.com/patrickpaul-weavegrid/fs-api.git; \
    cd fs-api; \
    python -m venv venv
RUN /bin/bash -c "cd /var/code/fs-api && source venv/bin/activate && pip install -r requirements.txt"
WORKDIR /var/code/fs-api
CMD ["/bin/bash", "-c", "source venv/bin/activate && flask run -h 0.0.0.0 -p 5500"]