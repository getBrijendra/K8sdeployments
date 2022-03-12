FROM python:3.7
# Run commands from /app directory inside container
WORKDIR /app
# Copy requirements from local to docker image
COPY requirements.txt /app
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir
# Copy everything from the current dir to the image
COPY . .
# Run the app
#CMD [ "python3", 'app.py' ]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
