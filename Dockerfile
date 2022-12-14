#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b ultro https://github.com/oktetod/ultro /home/ultro/ \
    && chmod 777 /home/ultro \
    && mkdir /home/ultro/bin/

COPY ./sample.env ./.env* /home/ultro/

WORKDIR /home/ultro/

RUN pip install -r requirements.txt

CMD ["bash","y"]
