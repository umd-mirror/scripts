#!/bin/sh

curl http://mirror:d2ccd17f9974829623f6841641c3795c@localhost:8080/jenkins/job/$1/build?cause=SSH+Push

