# REST API Testing Framework

The framework was designed to run inside a `Docker` container to strip out the complexity of setting 
virtual environments, facilitate its distribution and avoid the infamous ***but it works on my machine*** conversation.

## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Make](https://www.gnu.org/software/make/)
- [Python 3.8 and up](https://www.python.org/downloads/release/python-380/)

## Setup instructions

1. Open a terminal

2. Change to your favorite local directory (i.e. `cd /opt`)

3. Clone the repository

```bash
git clone git@github.com:ruvaz/restapi_test.git
```
4. Change to the project root directory

```bash
cd /opt/restapi_test
```

5. Create a new file, name it `secrets.ini` and add the following contents

```bash
APP_URL=https://gorest.co.in/public/v2
ACCESS_TOKEN=88818aa58fd4a391ffb39423c61426ada0dd583e2cb4c70a805062d56554fbac
```


## Usage 

It is possible to run the tests automatically when loading the Docker image with the `make run` command, or it is also possible to run the Docken image in development mode to be able to interact with the terminal with the `make dev` command, this mode also allows make code changes and see the reflections immediately in container.

### Run the Docker image and run the tests automatically

This test automatically generates by default `7` users and a post for each user, it will also generate 1 to 4 comments randomly for each post. This value can be changed in Develop mode with the `--users` parameter.

To load the Docker image and automatically execute the tests, the following command must be executed.

```bash
make run
```

> You will see the logs at the information level by default, if you want to see the rest of the logs at the debug level you will have to run the Docker image in development mode.

> An HTML report will be stored in the path:  /opt/restapi_test/reports/restapi_test_report.html
In the same path you will find the log file: /opt/restapi_test/reports/restapi_test.log

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
- [Ruben Vazquez](https://github.com/ruvaz)
