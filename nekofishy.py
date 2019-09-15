import os,sys,thread,socket,random,string,time
from pprint import pprint

"""Config"""
BACKLOG = 50            
MAX_DATA_RECV = 4096   
CONN_DEV = []

def event(tag, msg):
    print(event_get_str(tag, msg))

def event_get_str(tag, msg):
    while(len(tag) < 5):
        tag += "-"
    return ("[" + tag + "]:\t\t" + msg)

def print_new_dev(client_addr):
    global CONN_DEV
    if not str(client_addr[0]) in CONN_DEV:
        event("CONN", "Device " + str(len(CONN_DEV) + 1) + ":::@" + str(client_addr[0]) + ":" + str(client_addr[1]) + " is connected!")
        CONN_DEV.append(str(client_addr[0]))

def get_dev_index(client_addr):
    global CONN_DEV
    i = 0
    while(i < len(CONN_DEV)):
        if CONN_DEV[i] == str(client_addr[0]):
            return str(i + 1)
    return str(len(CONN_DEV) + 1)

def random_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

try:
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    payloadGetText = f = open(os.path.join(__location__, "payloads\get.pld"), "r").read()
    payloadSendText = f = open(os.path.join(__location__, "payloads\send.pld"), "r").read()
    welcomeMsg = f = open(os.path.join(__location__, "res\welcome.msg"), "r").read()
except:
    event("ERROR", "Resources missing. Download this script with its contents again!")
    try:
        input()
    except:
        sys.exit(1)
    sys.exit(1)

"""Main execution"""
def main():
    print welcomeMsg

    # check the length of command running
    if (len(sys.argv) < 2):
        event("ALERT", "Using default port 12345")
        port = 12345
    else:
        port = int(sys.argv[1]) # port from argument

    event("INFO", "Connect devices through proxy: " + socket.gethostbyname(socket.gethostname()) + ":" + str(port))

    # host and port info.
    host = ""              # localhost
    
    event("INIT", "Initializing proxy")

    try:
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # associate the socket to host and port
        s.bind((host, port))

        # listen
        s.listen(BACKLOG)
    
    except socket.error, (value, message):
        if s:
            s.close()
        event("ERROR", "Could not init proxy. Port " + str(port) + " may already be in use")
        sys.exit(1)

    event("INFO", "Proxy initialized")
    event("EVENT", "Listening for Neko Atsume...")

    # get the connection from game client
    while 1:
        conn, client_addr = s.accept()
        thread.start_new_thread(proxy_thread, (conn, client_addr))
        
    s.close()
    

def proxy_thread(conn, client_addr):
    global payloadSendText

    # get the request from game client
    request = conn.recv(MAX_DATA_RECV)

    # parse the first line
    first_line = request.split('\n')[0]

    # get url
    url = first_line.split(' ')[1]

    if not (("nekoatsume" in url and "daily" in url) or ("nekoatsume" in url and "aiko" in url)):
        conn.close()
        sys.exit(1)
        
    # send to game client
    print_new_dev(client_addr)
    
    #if get password
    if("nekoatsume" in url and "daily" in url):
        conn.send(payloadGetText)

    #if enter password
    if("nekoatsume" in url and "aiko" in url):
        event("CHEAT", "Device " + get_dev_index(client_addr) + " requested fish")
        try:
            silver = input(event_get_str("INPUT", "Enter amount of silver fish to receive: "))
            gold = input(event_get_str("INPUT", "Enter amount of gold fish to receive: "))
            int(silver)
            int(gold)
        except:
            event("ERROR", "User input malformed.")
            conn.close()
            sys.exit(1)
        payloadBkp = payloadSendText
        payloadSendText = payloadSendText.replace("[EVENT_PLACEHOLDER]", random_string())
        payloadSendText = payloadSendText.replace("[SILVER_FISH]", str(silver))
        payloadSendText = payloadSendText.replace("[GOLD_FISH]", str(gold))
        conn.send(payloadSendText)
        payloadSendText = payloadBkp
        event("DONE", "Sent fish (" + str(silver) + "s, " + str(gold) + "g) to device " + get_dev_index(client_addr) + "!")
    conn.close()
    
if __name__ == '__main__':
    main()