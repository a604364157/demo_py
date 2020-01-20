from flask import Flask, request, json

from demo.flask.server.two_color import run_two_color

app = Flask(__name__)


@app.route("/", methods=["get"])
def hello():
    return "hello world"


@app.route("/run/ball", methods=["get"])
def run_ball():
    times = int(request.args.get("times"))
    if times is None:
        times = 1
    else:
        times = int(times)
    out = []
    for i in range(times):
        out.append(run_two_color())
    return json.dumps(out)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
