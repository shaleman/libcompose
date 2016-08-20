from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.environ["REDIS_NAME"], port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This page has been seen %s times. - %s\n' % (redis.get('hits'), socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
