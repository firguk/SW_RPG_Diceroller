#!/bin/bash

REPORT_PATH="./code_analysis_report.txt"

if ! type pylint3 > /dev/null
then
  echo "pylint3 is not install"
  exit 1
fi

# run test in the console 
find . -iname "*.py" | xargs pylint3 --output-format=colorized --reports=n ./src/*.py

# save report to a separated file for GCONF
find . -iname "*.py" | xargs pylint3 --disable=all --output-format=text ./src/*.py > $REPORT_PATH

echo "Report generated, see $REPORT_PATH"