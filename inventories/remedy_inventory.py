#!/usr/bin/env python3
import json
import sys
import os

def get_inventory():
    inventory_data_str = os.environ.get('INVENTORY_DATA', '{}')
    try:
        inventory_data = json.loads(inventory_data_str)
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {inventory_data_str}", file=sys.stderr)
        return {}

    return inventory_data  # Return the data as-is, it's already in the correct format

if __name__ == "__main__":
    inventory = get_inventory()
    print(json.dumps(inventory))
