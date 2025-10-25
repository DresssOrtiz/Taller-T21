import time, random, zmq
from pubs import config

ctx = zmq.Context.instance()
sock = ctx.socket(zmq.PUB)
endpoint = f"tcp://{config.BROKER_HOST}:{config.PORT_XPUB}"
sock.connect(endpoint)
print(f"[PUB TEMP] conectado a {endpoint}", flush=True)

while True:
    temp = round(20 + random.random() * 8, 2)
    msg = f"{config.TOPIC_TEMP} {temp}"
    sock.send_string(msg)
    print(f"[PUB TEMP] -> {msg}", flush=True)
    time.sleep(config.PERIOD_SEC)
