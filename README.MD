# REST API Testing Framework

The framework was designed to run inside a `Docker` container to strip out the complexity of setting 
virtual environments, facilitate its distribution and avoid the infamous ***but it works on my machine*** conversation.

## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop) 
- [Python 3.8 and up](https://www.python.org/downloads/release/python-380/)

## Setup instructions

- Clone the repository

- change to the project folder

- Open a terminal

- install python library virtualenv 
    `pip install virtulenv`

- create virualenv venv
    `python -m venv venv`

- load virtual venv
    `source /venv/Scripts/activate`

- install requirements.txt 
    `pip install -r requirements.txt`


 
## Usage 
 `sh suites/all_tests.sh`

```sh 
pytest --html=reports/restapi_test_report.html --self-contained-html -v -s --users 7 tests/
```

### Run the Docker image and run the tests automatically
 

###  Run Docker Image in develop mode [Optional]



In develop mode you can run the tests manually and execute the test with more parameters 

1. Start development environment

```bash
make dev
```
>This command will remove any existing `restapi_test` containers, build a new test/restapi_testfwk image, start a container, mount local code under /opt/restapi_test and provide a /bin/bash terminal.

2. Create the command line with your desired specifications for the tests.

| Parameter  | Posible Values                          |	Description |
| ------------- |-----------------------------------------|------------- |
| **--users** | default value is **1** could be **N** users | N number of users to create and their posts and comments |
| **--log-cli-level** | **info** or **debug**                   | log level info |
| **--html**  | reports/restapi_test_report.html        | path and name of html report file|

 * Example
```bash
pytest --html=reports/restapi_test_report.html --self-contained-html  --users 10  --log-cli-level=debug  tests/
```

> You will find an HTML report stored in the path:  /opt/restapi_test/reports/restapi_test_report.html
In the same path you will find the log file: /opt/restapi_test/reports/restapi_test.log


### Author
[Ruben Vazquez](https://github.com/ruvaz)
