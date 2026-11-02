import threading
import time

from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

resource = Resource(attributes={"service.name": "myapp"})
provider = TracerProvider(resource=resource)
provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(
            endpoint="https://CRIBL-URL-GOES-HERE:4317",
            insecure=True,
        )
    )
)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def hello():
    return "Hello, OTel!"

def emit_heartbeat_traces(interval_seconds=5):
    while True:
        with tracer.start_as_current_span("heartbeat"):
            pass
        time.sleep(interval_seconds)

if __name__ == "__main__":
    threading.Thread(target=emit_heartbeat_traces, daemon=True).start()
    app.run(port=8080)