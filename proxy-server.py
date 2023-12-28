import random
import subprocess
import socket

# Dummy list of MySQL nodes. This is kinda like pseudocode because I can't test it on AWS
# In Production this would obviously refer to real resources
nodes = {
    "master": "mysql-master-node",
    "slaves": ["mysql-slave-node-1", "mysql-slave-node-2", "mysql-slave-node-3"]
}

def direct_hit():
    """ Direct Hit strategy: Always forwards to the master node. """
    return nodes["master"]

def random_choice():
    """ Random strategy: Randomly selects a slave node. """
    return random.choice(nodes["slaves"])

def ping_node(node):
    """ Pings a node and returns the response time. """
    try:
        response = subprocess.check_output(
            ['ping', '-c', '1', node],
            stderr=subprocess.STDOUT,  # Capture standard error in the output
            universal_newlines=True  # Return string instead of bytes
        )
        return True
    except subprocess.CalledProcessError:
        return False

def customized_choice():
    """ Customized strategy: Selects the node with the best (lowest) ping time. """
    alive_nodes = [node for node in nodes["slaves"] if ping_node(node)]
    return min(alive_nodes, key=ping_node) if alive_nodes else None

def handle_request(request):
    """ Handle incoming request based on the chosen strategy. """
    # Example of selecting a strategy
    node_address = direct_hit()  # Replace with random_choice() or customized_choice() as needed
    node_address = customized_choice()
    # Here I would add the AWS/Server related Logic to forward the request to the chosen node.
    # This is for showing the concept only for my presentation
    print(f"Forwarding request to {node_address}")

# Example usage
handle_request("SELECT * FROM my_table;")