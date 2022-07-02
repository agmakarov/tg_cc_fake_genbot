FROM python:3

COPY . ./cc_fake_gen
WORKDIR ./cc_fake_gen

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]