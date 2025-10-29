# broker/config.py
BROKER_HOST = "0.0.0.0"   # acepta conexiones de cualquier VM
PORT_XSUB   = 5560         # donde se conectan los publishers
PORT_XPUB   = 5561         # donde se conectan los subscribers

# Tópicos base del sistema
TOPICS = {
    "sensor.temp": "Temperatura ambiente (°C)",
    "sensor.hum":  "Humedad relativa (%)"
}
