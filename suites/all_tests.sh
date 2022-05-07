#!/bin/sh
set -eux
pytest --html=reports/all_tests.html --self-contained-html -v -s --users 7 tests/
