#!/bin/sh
while [ 1 ]; do curl -s $APP_SVC_NAME:8000; sleep 1; done
