# base image  
FROM python:3.8-slim-buster   

# set work directory  
RUN mkdir /server  

# where your code lives  
WORKDIR /server  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies  
COPY pyproject.toml .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev


# Copy all files
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT server.wsgi:application
