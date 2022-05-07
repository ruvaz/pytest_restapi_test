# REST API Testing Framework

The framework was designed to run inside a `Docker` container to strip out the complexity of setting virtual environments, facilitate its distribution and avoid the infamous ***but it works on my machine*** conversation.

## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Make](https://www.gnu.org/software/make/)
- [Python 3.8 and up](https://www.python.org/downloads/release/python-380/)

## Setup


1. Open a terminal

2. Change to your favorite local directory (i.e. `cd /opt`)

3. Clone the repository

```bash
git clone git@github.com:ruvaz/restapi_test.git
```
4. Change to the project root directory

```bash
cd /opt/basic-restapi-test
```

5. Create a new file, name it `secrets.ini` and add the following contents

```bash
APP_URL=https://gorest.co.in/public/v2
ACCESS_TOKEN=88818aa58fd4a391ffb39423c61426ada0dd583e2cb4c70a805062d56554fbac
```

6. Run the application

```bash
make run
```


7. Start development environment [Optional]

```bash
make dev
```
