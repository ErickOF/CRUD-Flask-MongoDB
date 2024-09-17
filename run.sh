HOST=127.0.0.1
PORT=5000
DEBUG=--debug

flask --app app run --host $HOST --port $PORT $DEBUG
