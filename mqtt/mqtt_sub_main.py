import paho.mqtt.client as mqtt

def on_connect( client, userdata, flags, rc ):
  print("Connect with result code " + str(rc) )  #결과 코드로 연결 str - 연결 결과를 표시해줌
  client.subscribe("Smart/Myhome/#")  #클라이언트가 받는 위치 지정

def on_message( client, userdata, msg ):
  str_msg = str(msg.payload)
  print( msg.topic +" "+str_msg)

  if (msg.topic == "Smart/Myhome/Rasp/Length"):
    int_msg = int(str_msg[2:len(str_msg)-1])
    print("length", int_msg)
  
  if (msg.topic == "Smart/Myhome/Rasp/Width"):
    int_msg = int(str_msg[2:len(str_msg)-1])
    print("width", int_msg)

  if (msg.topic == "Smart/Myhome/Rasp/Neopixel"):
    print("Neopixel color")

client = mqtt.Client( )
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('hyunsu', '0223')
client.connect("localhost", 1883, 60)
client.loop_forever( )
