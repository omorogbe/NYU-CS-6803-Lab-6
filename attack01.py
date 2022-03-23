import socket


def test_case_2():
    infant_port = 23456 # Infant port
    password = b'!Q#E%T&U8i6y4r2w' # password

    while True:
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.sendto(b"AUTH %s" % password, ("127.0.0.1", infant_port))
        msg, addr = s.recvfrom(1024)
        s.close()

def test_case_3():
    infant_port = 23456  # Infant port
    password = b'!Q#E%T&U8i6y4r2w'  # password

    # The authorized client is using the password to authenticate into the server and get the token for further communication
    authorized_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    authorized_client.sendto(b"AUTH %s" % password, ("127.0.0.1", infant_port))
    msg, addr = authorized_client.recvfrom(1024)
    authorized_client.close()

    # Token is retrieved and as the token is not encrypted anyone can use it to retrieve information from server.
    token = msg.strip()

    # Now the unauthorized client will create a connection that will not authenticate but get temperature from server using the token
    unauthorized_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    unauthorized_client.sendto(b"%s;GET_TEMP" % token, ("127.0.0.1", infant_port))
    msg, addr = unauthorized_client.recvfrom(1024)
    m = msg.decode("utf-8")
    print((float(m)))


test_case_3()
test_case_2()
