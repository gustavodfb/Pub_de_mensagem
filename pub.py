from is_wire.core import Channel, Message

# Conect to the broker
channel = Channel("amqp://guest:guest@10.10.0.91:5672")

message = Message()
#message.body = "Gustavo@Hello!".encode('latin1')
message.reply_to = "Gustavo"
message.correlation_id = 123

while True:
    #Broadcast message to anyone interested (subscribed)
    msg = input("Escreva a msg: ")
    dest = input("Destino: ")
    message.body = msg.encode('utf-8')
    channel.publish(message, topic=f"Aluno.{dest}")
