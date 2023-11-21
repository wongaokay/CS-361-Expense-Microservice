import zmq

def update_expense(cat_to_update, amount_to_subtract):
    """Updates category dictionary given cat_to_update (str) and amount_to_subtract (int) using microservice"""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Request Microservice
    # Assign current_expense to variable given cat_to_update
    current_expense = category_dict[cat_to_update]

    socket.send_string(f"User requesting to update {cat_to_update}")
    if socket.recv_string() == "REQUEST_DATA":
        data = {"current_expense": current_expense, "amount_to_subtract": amount_to_subtract}
        socket.send_json(data)

    # Receive Microservice
    updated_expense = int(socket.recv_string())

    # Update dictionary
    category_dict[cat_to_update] = updated_expense

    print(f"Subtracted ${amount_to_subtract} from {current_expense}")
    print(f"{cat_to_update}: {category_dict[cat_to_update]}")


category_dict = {
    'Groceries': 195,
    'Rent': 1200
}


if __name__ == "__main__":
    for request in range(2):
        update_expense("Groceries", 100)
