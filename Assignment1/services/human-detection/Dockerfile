# we start from slim python images, which already has all the requirements for python
FROM python:slim

# this will be working directory inside of the image
WORKDIR /usr/src/app

# copy python library requirements.txt 
COPY requirements.txt ./

# instal those requirements
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update 
RUN apt-get install -y curl

# copy source files
COPY . .

# execute application
CMD ["python", "./human-detection.py"]