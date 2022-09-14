FROM alpine:latest
RUN mkdir /app
WORKDIR /app

RUN apk add --no-cache bash py3-pip git

COPY ../requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check \
    --no-cache-dir install \
    -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

## To create a standalone container we could uncomment the COPY
# COPY . .

# To keep the container alive.
CMD tail -f /dev/null
