# Test-Task-QA-SF
A sample of a RESTful api and a testsuite testing it

## Task
The task was for me to build a an automated test suite for a RESTful API that simulates a trading platform with WebSocket support. Also I was required to dockerize both the test-Suite and the server.

### Basic description of files

  The project consists of 2 python scripts, 2 .bat files, 1 dummy database file with a json format and 1 Dockerfile with the necessary commands for containerizing the result.

The python script with the name "api_server.py" creates the RESTful API server, and covers the basic requirements 1-5 as well as the 1st advanced requirement mentioned in the pdf file with the instructions.
The python script with the name "Test_Suite.py" tests the api server and produces an html report

### A) Steps for executing the api server & test suite manually
1. Clone the repo with all existing files inside.
2. First double-click and run the "run_server.bat" file
3. Second double-click and run the "run_test.bat" file
#### Prerequisites for manual execution
a) Python version > 3.6
b) Installed fastapi --> pip install fastapi
c) Installed pydantic --> (usually installed with fastapi) pip install pydantic
d) Installed typing -->pip install typing
e) Installed asyncio --> pip install asyncio
f) Installed uvicorn --> pip install uvicorn
g) Installed requests --> pip install requests

### B) Steps for executing the api server & test suite with container
Unfortunately I was not able to produce a valid dockerized image, due to implementing everything in a windows 7 platform and experiencing difficulties with it. On the other hand i have created a Dockerfile containing all the necessary commands for the creation of the image file. Next, the steps to create the container and execute it are explained in due detail.
#### Steps for dockerizing
a) Install Docker client from https://www.docker.com/get-started/
b) navigate with cmd to the folder where the repo has been created
c) run on cmd " docker build -t random_name-docker . "// The . at the end of the command specifies that the image will be created in the specified folder
d) run on cmd " docker run random_name-docker . "
