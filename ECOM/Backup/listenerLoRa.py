#!/usr/bin/python3
import paho.mqtt.client as mqtt
import pymysql
import json
import base64
from sae503_bdd_set import *
from sae503_bdd_get import *
# Paramètres de connexion à la base de données
db_config = {
    'host': '192.168.1.110',
    'user': 'root',
    'password': 'tpRT9025',
    'database': 'ecomddb',
}

# Définir les variables
ID = None
adresseIP = None

# Fonction de rappel lors de la réception d'un message MQTT
def on_message(client, userdata, msg):
    global ID, adresseIP

    # Décoder le message
    message = msg.payload.decode("utf-8")
    message_json=json.loads(message)
    try:
        device_id=message_json["end_device_ids"]["device_id"]
        frm_payload=message_json['uplink_message']['frm_payload']
        frm_payload_decoded=base64.b64decode(frm_payload).decode('utf-8')
        if ('FALSE' in str(execute_stored_procedure("GET_euid",device_id))):
            add_objet(2,device_id,"true","RESULTAT",device_id)
        executer_procedure(int(frm_payload_decoded),'V',device_id)
    except Exception as e:
        print(e)
        pass

# Configurer le client MQTT
client = mqtt.Client()
mqtt_username="sae601iom"
mqtt_password = "NNSXS.WDSMKODI6HI6QLYTZX4B25GDQMOWKGUSJUWASWA.XDSXU3IAGJN7XZWFBDA2ZUM3SIMIF25PYDQKOWMLIHMUFEVVHGPA"
client.username_pw_set(username=mqtt_username, password=mqtt_password)
client.on_message = on_message
# Remplacez "localhost" par l'adresse IP de votre broker MQTT
broker_address = "eu1.cloud.thethings.network"
client.connect(broker_address, 1883, 60)

# S'abonner au topic "ipDiscover"
client.subscribe("v3/sae601iom@ttn/devices/#")

# Démarrer la boucle MQTT
client.loop_forever()
