from flask import Flask
from flask import request
from flask import jsonify
from google.cloud import datastore
import time

app = Flask(__name__)
client = datastore.Client()

magicKey = "{PUT_YOUR_KEY_HERE}"

@app.route('/log/<ipOwner>', methods = ['POST'])
def logIp(ipOwner):
    if ipOwner is None or ipOwner == '' or len(ipOwner) > 10:
        return '-2', 403
    if request.headers['magic'] == magicKey:
        ip = datastore.Entity(client.key('IpOwner', ipOwner))
        ip.update({
            'ip': request.headers['x-appengine-user-ip'],
            'update': time.time()
        })
        client.put(ip)
        return '', 200
    return '-1', 403

@app.route('/ip/<ipOwner>', methods = ['GET'])
def getIp(ipOwner):
    if ipOwner is None or ipOwner == '' or len(ipOwner) > 10:
        return request.headers['x-appengine-user-ip']
    if request.method == 'GET' and request.headers['magic'] == magicKey:
        key = client.key('IpOwner', ipOwner)
        entity = client.get(key)
        if entity is None:
            return 'Not found'
        return f'{ipOwner}: {entity["ip"]}<br/>Last Update: {entity["update"]}', 200
    return '-1', 403

@app.route('/ip', methods = ['GET'])
def getCurrentIp():
    return request.headers['x-appengine-user-ip']

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)