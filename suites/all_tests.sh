#!/bin/sh
set -eux
pytest --html=reports/restapi_test_report.html --self-contained-html -v -s tests/
