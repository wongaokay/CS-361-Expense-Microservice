import zmq

def update_expense(cat_to_update, amount_to_subtract):
    """Both request and receives microservice"""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Request Microservice
    # Assign current_expense to variable given cat_to_update
    current_expense = category_dict[cat_to_update]

    socket.send_string("User requesting to update category")
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
    for request in range(1):
        update_expense("Rent", 50)
