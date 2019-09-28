FROM alpine:3.9

WORKDIR /src

# Update
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Install app dependencies
# none in my case
RUN pip install telepot pynamodb

COPY config.json /src/config.json
COPY *.py .

CMD ["python3", "/src/bot.py", "-p 33000"]