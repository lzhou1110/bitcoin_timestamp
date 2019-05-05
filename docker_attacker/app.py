from binascii import hexlify, unhexlify
from hashlib import sha256
from io import BytesIO
import random
import socket
import struct
import time
import hashlib


def makeMessage(cmd, payload):
    magic = "F9BEB4D9".decode("hex") # Main network
    command = cmd + (12 - len(cmd)) * "\00"
    length = struct.pack("I", len(payload))
    check = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    return magic + command + length + check + payload


def versionMessage(recv_ip, from_ip):
    version = struct.pack("i", 60002)
    services = struct.pack("Q", 0)
    timestamp = struct.pack("q", time.time())
    addr_recv = struct.pack("Q", 0)
    addr_recv += struct.pack(">16s", recv_ip)
    addr_recv += struct.pack(">H", 8333)
    addr_from = struct.pack("Q", 0)
    addr_from += struct.pack(">16s", from_ip)
    addr_from += struct.pack(">H", 8333)
    nonce = struct.pack("Q", random.getrandbits(64))
    user_agent_bytes = struct.pack("B", 0)
    height = struct.pack("i", 0)
    payload = version + services + timestamp + addr_recv + addr_from + nonce +user_agent_bytes + height
    return payload



def print_current_machine_time():
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Local time:", local_time)


def attack_someone():
    print('Host name: {}'.format(socket.gethostbyname(socket.gethostname())))


def read_a_message(sock):
    header = BytesIO(sock.recv(24))
    version = hexlify(header.read(4))
    command = header.read(12).decode().replace('\x00', '').upper()
    payload_size = struct.unpack("I", header.read(4))[0]
    checksum = hexlify(header.read(4))
    payload = sock.recv(payload_size)
    return {'message_type': command, 'payload': payload}


if __name__ == "__main__":
    time.sleep(10)
    print('Starting to attack')
    print_current_machine_time()
    user_agent_to_send = 'agentalex'
    version = struct.pack("i", 70015)  # corresponds to 0.15
    services = struct.pack("Q", 0)  # this "node" does nothing
    timestamp = struct.pack("Q", (int(time.time())))
    addr_recv_services = struct.pack("q", 0)
    addr_recv_ip = struct.pack(">16s", b'127.0.0.1')
    addr_recv_port = struct.pack(">H", 8333)
    addr_trans_services = struct.pack("Q", 0)
    addr_trans_ip = struct.pack(">16s", b'127.0.0.1')
    addr_trans_port = struct.pack(">H", 8333)
    nonce = struct.pack("Q", random.getrandbits(64))
    user_agent_bytes = struct.pack("<B", len(user_agent_to_send))
    user_agent = user_agent_to_send.encode()
    starting_height = struct.pack("i", 0)
    relay = struct.pack("?", False)

    payload = version + services + timestamp + addr_recv_services + \
              addr_recv_ip + addr_recv_port + addr_trans_services + \
              addr_trans_ip + addr_trans_port + nonce + user_agent_bytes + \
              user_agent + starting_height + relay

    network = unhexlify("F9BEB4D9")  # mainnet
    command = str.encode('version'.ljust(12, '\00'))
    payload_size = struct.pack("I", len(payload))
    checksum = sha256(sha256(payload).digest()).digest()[:4]
    full_version_message = network + command + payload_size + checksum + payload
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        some_existing_bitcoin_nodes = ["10.255.0.0"]
        sock.connect((random.choice(some_existing_bitcoin_nodes), 8333))
        sock.sendall(full_version_message)
        first_received_message = read_a_message(sock)
        print(f"Response: {first_received_message}")
    finally:
        sock.close()
