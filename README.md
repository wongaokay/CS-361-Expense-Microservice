# CS-361-Expense-Microservice

## Example: Let's say this was the current category_dict. How would you subtract $50 from Groceries?
```python
category_dict = {'Groceries': 195}
```

## How to programmatically Request data from the update_expense microservice

example call:
```python
    import zmq
    
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Subtracting $50 from Groceries
    current_expense = category_dict["Groceries"]
    amount_to_subtract = 50

    socket.send_string("User requesting to update category")
    if socket.recv_string() == "REQUEST_DATA":
        data = {"current_expense": current_expense, "amount_to_subtract": amount_to_subtract}
        socket.send_json(data)
```

## How to programmatically Receive data from the update_expense microservice

example call:
```python
    ... continuation of request ...

    # Recieve the request and convert the string to integer  
    # Updated expense for Groceries is $145
    updated_expense = int(socket.recv_string())

    # Now, update groceries category with the new value
    category_dict["Groceries"] = updated_expense
```
