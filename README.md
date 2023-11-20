# CS-361-Expense-Microservice

## How to programmatically Request data from the update_expense microservice

example call:
```python
    import zmq
    
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    
    # Subtracting $50 from $300
    current_expense = 300
    amount_to_subtract = 50

    socket.send_string("User requesting to update category")
    if socket.recv_string() == "REQUEST_DATA":
        data = {"current_expense": current_expense, "amount_to_subtract": amount_to_subtract}
        socket.send_json(data)
```

## How to programmatically Receive data from the update_expense microservice
