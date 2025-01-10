#!/usr/bin/python3
import os
import yaml
import json
import requests

# A basic script that reads the yml files in the 'devices' directory and populates NetBox
# With the device types and relevant interface templates via the NetBox API

# Function to post data to the NetBox API
def post_data(api: str, content: dict, name: str = "[Undefined]") -> None:
    url = f"http://netbox:8080/api/{api}/"
    # Bad practice to hardcode the API token, but this is a basic example
    api_token = "a4bd2e9bf74869feb061eba14b090b4811353d9f"
    nb_headers = {
        "Authorization": f"Token {api_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    nb_content = json.dumps(content)
    response = requests.post(url, headers=nb_headers, data=nb_content)
    if response.status_code == 201:
        print(f"{name} API call successful: {response.status_code}")
    else:
        print(f"{name} API call failed with content: {url}, {nb_content}")
        print(f"{name} API call response: {response.status_code}, {response.text}")
    

def main():
    # Static variables
    directory_path = "devices"
    yaml_list = []
    # Pull in yaml data from the files in the devices directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            file_path = os.path.join(directory_path, filename)
            print(f"Importing {filename}")
            with open(file_path, 'r') as file:
                try:
                    yaml_data = yaml.safe_load(file)
                    yaml_list.append(yaml_data)
                except yaml.YAMLError as exc:
                    print(f"Error loading {filename}: {exc}")
    # Post imported data into NetBox using the relevant API endpoints depending on the data
    # For this we need to exclude some dictionary keys for the device_types api and then
    # also loop through the ports for the template APIs if the relevant keys exist
    
    # Start with our blank data structures
    device_types = []
    device_interfaces = {}
    # Work through the yaml data device by device
    for device in yaml_list:
        device_type_data = {}
        # Add an inner dictionary to our device_interfaces dictionary with the device slug as the key
        device_interfaces[device["slug"]] = {}
        for key, value in device.items():
            # Check if we're in an inner list (i.e. our list of interfaces)
            if isinstance(value, list):
                # Create our device_interfaces list for our device and interface type
                device_interfaces[device["slug"]][key] = []
                # Our value is a list of dictionaries, but we need to add a decive_type inner dictionary
                # to each item in the list as well or we get the error:
                # "Related objects must be referenced by numeric ID or by dictionary of attributes."
                # and in this instace we don't want to do a separate GET call just to get the ID
                for port in value:
                    port["device_type"] = {}
                    port["device_type"]["model"] = device["model"]
                    port["device_type"]["slug"] = device["slug"]
                    device_interfaces[device["slug"]][key].append(port)
            # If we're not in a list, we can just add the k/v pair to our device_type_data dictionary
            else:
                # Ditto for the manufacturer field in the device_types POST call
                if key == "manufacturer":
                    device_type_data["manufacturer"] = {}
                    device_type_data["manufacturer"]["name"] = device[key]
                    device_type_data["manufacturer"]["slug"] = device[key].lower().replace(" ", "-")
                else:
                    device_type_data[key] = device[key]
        device_types.append(device_type_data)
    # Send our data to the NetBox API
    print("Sending below data to NetBox API")
    print(f"Device Types: {json.dumps(device_types, indent=2)}")
    print(f"Device Interfaces: {json.dumps(device_interfaces, indent=2)}")
    # Start with our device types
    for device in device_types:
        name = f"[{device['model']}]"
        post_data("dcim/device-types", device, name)
        # Then based on the key in our device interfaces, send the data to the relevant API
        for key, value in device_interfaces[device["slug"]].items():
            name = ""
            match key:
                case "interfaces":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/interface-templates", data, name)
                case "console-ports":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/console-port-templates", data, name)
                case "power-ports":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/power-port-templates", data, name)
                case "power-outlets":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/power-outlet-templates", data, name)
                case "rear-ports":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/rear-port-templates", data, name)
                case "front-ports":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/front-port-templates", data, name)
                case "device-bays":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/device-bay-templates", data, name)
                case "module-bays": 
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/module-bay-templates", data, name)
                case "console-server-ports":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/console-server-port-templates", data, name)
                case "inventory-items":
                    for data in value:
                        name = f"[{device['model']} - {key} - {data['name']}]"
                        post_data("dcim/inventory-item-templates", data, name)
                case _:
                    print(f"Invalid key found: {key}")


if __name__ == "__main__":
    main()