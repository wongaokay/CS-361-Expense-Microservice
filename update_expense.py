import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Update Expense Microservice")
while True:
    # Receive request from client
    received_request = socket.recv().decode('utf-8')
    print(received_request)

    time.sleep(.5)

    # Request user data from client {"current_expense": ?, "amount_to_subtract: ?"}
    print("Requesting data from client")
    socket.send_string("REQUEST_DATA")
    data = socket.recv_json()

    current_expense = data["current_expense"]
    amount_to_subtract = data["amount_to_subtract"]

    # Calculate updated expense
    updated_expense = current_expense - amount_to_subtract
    if updated_expense < 0:
        updated_expense = 0

    time.sleep(.5)

    # Send back updated expense
    print(f"Updated expense: ${updated_expense}")
    socket.send_string(str(updated_expense))
