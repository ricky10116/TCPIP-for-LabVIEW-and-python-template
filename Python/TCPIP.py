
import socket ,time


address = ('127.0.0.1',21) 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()
s.bind(address) 
s.listen(1)
connection, addr = s.accept()
 
print("Start") 

while True:      
       
       time.sleep(0.1)
       Data=connection.recv(20)      
      
       if Data == b"close\r\n":   # 客戶端要停止...
           break
       elif Data == b"Hello\r\n":
           print("Data=",Data)
       elif Data == b"WR\r\n":
           print("Data=",Data) 
           connection.send(b"11111111111111\r\n")
       elif Data == b"WR2\r\n":
           print("Data=",Data) 
           connection.send(b"NationInstruments!!!\r\n") 
       elif not Data:             # 如果客戶端斷線...
           break
      
print("END")        

s.close()