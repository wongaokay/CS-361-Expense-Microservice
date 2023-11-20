# CS-361-Expense-Microservice

## Example Dictionary
```python
category_dict = {'Groceries': 195, 'Rent': 1200}
```

## Both Requesting and Receiving data in a single function
```python
import zmq

def update_expense(cat_to_update, amount_to_subtract):
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
```
example call:
```
# Subtracts $100 from Rent, and updates category_dict
update_expense("Rent", 100)
```

## Further explanations
### How to programmatically Request data from the update_expense microservice
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

### How to programmatically Receive data from the update_expense microservice
```python
    ... continuation of request ...

    # Recieve the request and convert the string to integer  
    # Updated expense for Groceries is $145
    updated_expense = int(socket.recv_string())

    # Now, update groceries category with the new value
    category_dict["Groceries"] = updated_expense
```

