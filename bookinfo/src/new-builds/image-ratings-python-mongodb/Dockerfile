# Build ratings module backed by database: PostgreSQL or MongoDB Atlas
# Version: 1.0
# Author: Naresh Bandi
FROM python:3.7.0
WORKDIR /
COPY packages /packages
WORKDIR /packages
RUN pip3 install -vvv --no-cache-dir -r require.txt
COPY ratings-python.py /opt/microservices/
EXPOSE 9080
WORKDIR /opt/microservices
CMD ["python", "ratings-python.py", "9080"]
USER 1000

