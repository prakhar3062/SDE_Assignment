# SDE_Assignment
It is an api built with the flask package. It also uses the Pillow Package. It will send the generated image array in response to the api call according to the parameters provided.Most of the Server part is the main.py file.
in the api call.<br> 
# Installation
* Install the Flask package 
* Install the Pilow package
* Run the commannd in the terminal ```build.sh```
* Run the command in the terminal  ```run.sh```
# USAGE
After installing all dependencies and libraries, run the main.py file to start the server in the localhost.
The container expects an HTTP POST request to /generate_image, with parameters resembling the following:
* width: the width of the image array in pixels (integer)
* height: the height of the image array in pixels (integer)
* color: the color of the image (string, one of 'red', 'green', 'blue')
* format: the format of the image (string, one of 'jpeg', 'png', 'gif') 
Response will be an generated image in the specified format and of MIME Type

# TroubleShooting
### 400 Bad Request 
Make sure you have passed the parameters in the specified format as mentioned above.
