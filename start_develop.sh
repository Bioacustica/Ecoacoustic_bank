#!/bin/bash

echo "Se ejecuta el start_develop.sh"

java -jar schemaspy-6.1.0.jar -configFile schema_spy.properties
/bin/sh -c "jupyter lab --ip='0.0.0.0' --port=8888 --NotebookApp.token='' --no-browser --allow-root"