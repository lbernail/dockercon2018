from flask import Flask,request
from socket import gethostname,gethostbyname
from os import getenv

app = Flask(__name__)
version = getenv('VERSION', 'Unknown')
alive = True
ready = True

@app.route('/')
def containerInfo():
    hostname = gethostname()
    hostip = gethostbyname(hostname)
    clientip = request.environ['REMOTE_ADDR']
    
    content = 'Container: {0:16}| Source: {1:16}| Version: {2}\n'.format(hostip,clientip,version)
    return content

@app.route('/alive')
def is_alive():
    global alive
    return "Alive : {0}".format(alive), 200 if alive else 503

@app.route('/ready')
def is_ready():
    global ready
    return "Ready : {0}".format(ready), 200 if ready else 503

@app.route('/toggleAlive')
def toggle_alive():
    global alive
    alive = not alive
    return "Alive changed to: {0}".format(alive)

@app.route('/toggleReady')
def toggle_ready():
    global ready
    ready = not ready
    return "Ready changed to: {0}".format(ready)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
