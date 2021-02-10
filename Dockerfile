FROM python:3.5.3 AS build-env

WORKDIR /app/

ADD . .

RUN pip install -r ./requirements.txt


FROM gcr.io/distroless/python3

COPY --from=build-env /app /app
COPY --from=build-env /usr/local/lib/python3.5/site-packages/ \
 /usr/lib/python3.5/.

WORKDIR /app/

CMD ["show_open_food_trucks.py"]