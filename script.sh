#!/bin/bash

build() {
    docker build -t finalproject-image .
    docker run -d --name container finalproject-image
}

setup() {
    echo "Executing environment setup..."

    docker exec container python3 setup.py
    docker exec container ./deploy.sh
}

send_requests() {
    echo "Running benchmark..."
    docker exec container python3 request_sender.py
}

teardown() {
    echo "Terminating environment..."

    docker exec container python3 teardown.py
}

kill_container() {
    docker kill container
    docker rm container
}

case "$1" in
    "build")
        build
        ;;
    "setup")
        setup
        ;;
    "send-requests")
        send_requests
        ;;
    "teardown")
        teardown
        ;; 
    "kill")
        kill_container
        ;;
esac


