FROM python:3.8

ARG VERSION
ARG BUILD_DATE

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.version=$VERSION \
      org.label-schema.name="PrometheusExport" \
      org.label-schema.description="Prometheus HTTP(S) check metrics exporter"

RUN echo $VERSION > image_version
RUN echo $BUILD_DATE > build_date

ENV HTTP_URIS="https://httpstat.us/200 https://httpstat.us/503"
 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
 
COPY app.py /

USER 1000
 
ENTRYPOINT ["uwsgi"]
 
CMD ["--http", "0.0.0.0:8000", "--wsgi-file", "app.py", "--callable", "app_dispatch"]
