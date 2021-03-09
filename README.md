
# SumAPI-Flask
> - A flask API which sums two numbers and returns the result.
> - Dockerfile to run on all machines
---
#### Sum API:


In the main part of this python file the API will be hosted on `0.0.0.0` with port of `8000`.
The `return_sum()` function works as a function which routes on `/sum` endpoint with POST method and returns a JSON format data as the result.
This an example of a POST request and the response on postman:

![POST request and JSON response ](https://uupload.ir/files/09al_screenshot_from_2021-03-09_16-37-23.png) 		 		                                          

---
### Run With Docker:
#### Dependencies:
- You should have docker installed on your machine

#### Build and run:
To create docker image, on directory which Dockerfile exists, use command like this:

    docker build -t <image_name> .
Run the image:

    docker run -p 8000:8000 <image_name>:latest

