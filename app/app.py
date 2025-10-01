from flask import Flask, jsonify
import psutil
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Server Performance Stats API", "status": "running"})

@app.route('/stats')
def stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    hostname = socket.gethostname()

    return jsonify({
        "cpu_usage": f"{cpu}%",
        "memory_usage": f"{memory}%",
        "disk_usage": f"{disk}%",
        "hostname": hostname
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

