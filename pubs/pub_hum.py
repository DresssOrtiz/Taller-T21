import time, random, zmq
from pubs import config
ctx = zmq.Context.instance()
sock = ctx.socket(zmq.PUB)
sock.connect(f"tcp://{config.BROKER_HOST}:{config.PORT_XSUB}")
print("[PUB HUM] conectado")
while True:
    v = round(40 + random.random()*20, 2)
    msg = f"{config.TOPIC_HUM} {v}"
    sock.send_string(msg)
    print(msg, flush=True)
    time.sleep(config.PERIOD_SEC)
