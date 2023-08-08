FROM  python:3.8.17-alpine3.18
COPY . /app
WORKDIR /app
RUN pip config set global.disable-pip-version-check true && pip install -r requirements.txt
ENV m=${m} c=${c} t=0.01
RUN echo "memory: ${m}, cpu: ${c}, t: $t"
ENTRYPOINT python app.py --m=$m --c=$c --t=$t
