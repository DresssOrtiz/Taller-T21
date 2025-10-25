import time, random, zmq
from pubs import config

ctx = zmq.Context.instance()
sock = ctx.socket(zmq.PUB)
endpoint = f"tcp://{config.BROKER_HOST}:{config.PORT_XPUB}"
sock.connect(endpoint)
print(f"[PUB HUM] conectado a {endpoint}", flush=True)

while True:
    hum = round(40 + random.random() * 20, 2)
    msg = f"{config.TOPIC_HUM} {hum}"
    sock.send_string(msg)
    print(f"[PUB HUM] -> {msg}", flush=True)
    time.sleep(config.PERIOD_SEC)
