from structure import structure
import json

def initiate_tools():
    return [structure.Tool('Screw'), structure.Tool('Pull'), structure.Tool('Push'),
            structure.Tool('Unpin'), structure.Tool('Pin')]



def read_tools_from_json(filename):
    # Read the JSON file
    with open(filename, 'r') as file:
        data = json.load(file)

    # Initialize a list to hold Tool objects
    tools = []

    # Iterate over the list of tool names and create Tool objects
    for tool_name in data.get("tools", []):
        tools.append(structure.Tool(name=tool_name, type=""))

    return tools