import time, random, zmq
from pubs import config
ctx = zmq.Context.instance()
sock = ctx.socket(zmq.PUB)
sock.connect(f"tcp://{config.BROKER_HOST}:{config.PORT_XSUB}")
print("[PUB TEMP] conectado")
while True:
    v = round(20 + random.random()*8, 2)
    msg = f"{config.TOPIC_TEMP} {v}"
    sock.send_string(msg)
    print(msg, flush=True)
    time.sleep(config.PERIOD_SEC)
