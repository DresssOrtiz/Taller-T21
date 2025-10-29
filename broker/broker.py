"""
Broker de Mensajería - Patrón Publicador/Suscriptor (ZeroMQ)

Responsable: Persona 1
Recibe mensajes desde los publicadores (XSUB)
y los distribuye a los suscriptores (XPUB)
"""

import zmq
import time
from broker import config

def start_broker():
    ctx = zmq.Context.instance()

    # Socket que recibe de los publishers
    xsub = ctx.socket(zmq.XSUB)
    xsub.bind(f"tcp://*:{config.PORT_XSUB}")

    # Socket que reenvía a los subscribers
    xpub = ctx.socket(zmq.XPUB)
    xpub.bind(f"tcp://*:{config.PORT_XPUB}")

    print("==========================================")
    print(" ZeroMQ Broker iniciado ")
    print(f" Esperando publishers en puerto {config.PORT_XSUB}")
    print(f" Esperando subscribers en puerto {config.PORT_XPUB}")
    print("------------------------------------------")
    for topic, desc in config.TOPICS.items():
        print(f"  • {topic}: {desc}")
    print("==========================================\n")

    # Proxy interno: reenvía los mensajes entre XSUB y XPUB
    try:
        zmq.proxy(xsub, xpub)
    except KeyboardInterrupt:
        print("\n[Broker] Finalizando...")
    finally:
        xsub.close()
        xpub.close()
        ctx.term()

if __name__ == "__main__":
    start_broker()
