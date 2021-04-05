import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '10.66.96.21'#socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
def register():
    number = input('enter your phone number:')
    files = open('customerdetails','a')
    files.write(number)
    files.write(',')
    files.write('\n')
    files.close()
    print('received your information')
    print('==========================================')
    print('we bringing you back to the menu')
    menu(number)
def login():
    number = input('enter your registered phone number:')
    files = open('customerdetails','r')
    for row in files:
        field = row.split(",")
        phoneno = field[0]
        
        if number == phoneno :
            break
        else :
            print('incorrect number')
            break
    print('loged in')

    menu(number)    
    
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
def menu(number):
    menu = ['KAIKROB (REGULAR)','KAIKROB (EXTRA)','KAIKROB (SUPEREXTRA)']
    cust_options = """ 
    Welcome to the customer interface! Please press the below options:
        
    0. Quit                 2. Customer signup
    1. View menu            3. Customer login

    Your Option:
    """        
        
    customer_options = int(input(cust_options))
    if customer_options == 0 :
        send(DISCONNECT_MESSAGE)

    if customer_options == 1 : 
        menu_option = """ 
        =========================== MENU =========================== 
        
               1:KAIKROB (REGULAR)
               2:KAIKROB (EXTRA)
               3:KAIKROB (SUPEREXTRA)
    
        Your Option:
        """        
        menu_options = int(input(menu_option))    
        if menu_options == 1 :
            send('ordered:'+menu[0] +'\n'+'customer number:'+ number)
        if menu_options == 2 :
            send('ordered:'+menu[1] +'\n'+'customer number:'+ number)
        if menu_options == 3 :
            send('ordered:'+menu[2] +'\n'+'customer number:'+ number)
    if customer_options == 2 :
        register()
    if customer_options == 3 :
        login()
number =  None
menu(number)


