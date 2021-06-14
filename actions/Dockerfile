#whatever version that suits you
FROM rasa/rasa-sdk:latest

#define the working directory of Docker container
WORKDIR /app 
#copy the requirements txt file with your dependencies in actions directory
COPY ./requirements.txt ./ 
#copy everything in ./actions directory (your custom actions code) to /app/actions in container
COPY ./ /app/actions
USER root
#install dependencies inside Docker container
RUN pip install -r requirements.txt 
RUN pip install Babel
USER 1001