FROM python:3.11-slim
WORKDIR /app
COPY install.sh run.sh ./
COPY app ./app
RUN chmod +x install.sh run.sh
RUN ./install.sh
CMD ["./run.sh"]
