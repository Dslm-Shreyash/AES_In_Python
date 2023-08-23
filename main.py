import socket
import AES_ENC as ae

port = 1234

        
joh = int(input("1 : Host \n2 : Join \nInput : "))    
if joh == 1:
      #!Server Part
    name = input("Enter Your Name : ")
    s = socket.socket()
    host = socket.gethostname()

    print('server will start on host : ',host)

    s.bind((host,port))
    print("server is bound successfully\n")

    s.listen(5)
   
    co,ad = s.accept()
    
    name = name.encode()
    co.send(name)
   
    client_name = co.recv(1024).decode()
    print(f'{client_name} Has Joined')
    
    
    while True :
        responce = input("\nYou : ").encode()
        key,eobj,ct=ae.encrypt(msg=responce)
        co.send(eobj)
        co.send(ct)
        print(f'" {responce.decode()} " Is Encrypted To : {ct} \n')
        co.send(key)
        
        e_obj = co.recv(1024)
        cipher_msg = co.recv(1024)
        print(f"Received  Cipher From ' {client_name} ' Is : ",cipher_msg)
        key = co.recv(1024)
        decrypted_msg=ae.decrypt(key=key,obj=e_obj,ct=cipher_msg)
        print(f"Decrypted Cipher From ' {client_name} ' Is : ",decrypted_msg)
        
else:
     name = input("Enter Your Name : ")
     client = input("Enter host name : ")
     s = socket.socket()
     s.connect((client,port))
    
     name = name.encode()
     s.send(name)
     print("\nconnected to server\n")
    
     client_name = s.recv(1024).decode()
     while True:
         
         e_obj = s.recv(1024)
         cipher_msg = s.recv(1024)
         print(f"Received  Cipher From ' {client_name} ' Is : ",cipher_msg)
         key = s.recv(1024)
         decrypted_msg = ae.decrypt(key=key,obj=e_obj,ct=cipher_msg)
         print(f"Decrypted Cipher From ' {client_name} ' Is : ",decrypted_msg)
         
         
         responce = input("\nYou : ").encode()
         key,eobj,ct=ae.encrypt(msg=responce)
         s.send(eobj)
         s.send(ct)
         print(f'" {responce.decode()} " Is Encrypted To : {ct} \n')
         s.send(key)
        
         