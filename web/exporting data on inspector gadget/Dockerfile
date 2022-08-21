FROM ubuntu:20.04

#Update the packages
RUN apt-get update

# Add Env Args for tzdata package
ARG DEBIAN_FRONTEND=noninteractive

# Install python
RUN apt-get install -y python3-pip python3

# Copy files
COPY ./src .
COPY ./document /document
COPY requirements.txt .

# Install requirements
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 2776

CMD ["gunicorn", "--bind", "0.0.0.0:2776", "wsgi:app"]