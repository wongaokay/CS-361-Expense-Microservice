# CS-361-Expense-Microservice

## Note
This microservice uses ZeroMQ for the communication pipeline. You'll need to install and import the python package `zmq`.

## Example Dictionary
```python
category_dict = {'Groceries': 195, 'Rent': 1200}
```

## Requesting and Receiving data in a single function (recommended)
This function is an example of requesting and receiving data from the microservice. Ideally, in the main program, another function will prompt the user what category they want to update (cat_to_update) and how much $ they want to subtract from the category (amount_to_subtract). For example, If the user wants to subtract $100 from Rent. Then the main program will call update_expense("Rent", 100). The microservice calculates and returns the updated expense, and the rest of the update_expense function updates the Rent category in the dictionary.

```python
import zmq

def update_expense(cat_to_update, amount_to_subtract):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Assign current_expense to variable given cat_to_update
    current_expense = category_dict[cat_to_update]

    # Request Microservice
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

## Further explanation
### How to programmatically Request data from the update_expense microservice
When requesting data from the microservice. First, send a string through the socket, such as "User requesting to update category." This will prompt the microservice to request the user data, which is a dictionary containing the category's current expense (current_expense) and the amount the user wants to subtract (amount_to_subtract).

example call:
```python
    import zmq
    
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Subtracting $50 from Groceries
    current_expense = category_dict["Groceries"]
    amount_to_subtract = 50

    socket.send_string(f"User requesting to update {cat_to_update}")
    if socket.recv_string() == "REQUEST_DATA":
        data = {"current_expense": current_expense, "amount_to_subtract": amount_to_subtract}
        socket.send_json(data)
```

### How to programmatically Receive data from the update_expense microservice
To receive data from the microservice, the main program receives the updated expense as a string. This can be converted into an integer and used to update the category in category_dict. Note, that the microservice isn't set up to have separate functions for requesting and receiving data. The update_expense function listed above is what I'd recommend using.

```python
    ... continuation of request ...

    # Recieve the request and convert the string to integer  
    # Updated expense for Groceries is $145
    updated_expense = int(socket.recv_string())

    # Now, update groceries category with the new value
    category_dict["Groceries"] = updated_expense
```

