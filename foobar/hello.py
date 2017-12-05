from flask import Flask, request, Response
from prometheus_client import Counter, generate_latest

app = Flask("foobar")
app.config.from_object(__name__)

# Create a metric to cound the number of runs on process_request()
c = Counter('requests_for_host', 'Number of runs of the process_request method', ['method', 'endpoint'])


@app.route('/hello')
def index():
    path = str(request.path)
    verb = request.method
    label_dict = {"method": verb,
                  "endpoint": path}
    c.labels(**label_dict).inc()
    return "Hello this big awesome new World!"


@app.route('/metrics')
def metrics():
    path = str(request.path)
    verb = request.method
    label_dict = {"method": verb,
                  "endpoint": path}
    c.labels(**label_dict).inc()
    return Response(generate_latest(),
                    mimetype=str('text/plain; version=0.0.4; charset=utf-8'))
