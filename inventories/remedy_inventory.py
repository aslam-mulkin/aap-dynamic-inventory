#!/usr/bin/env python3
import json
import sys
import os

def get_inventory():
    inventory_data_str = os.environ.get('INVENTORY_DATA', '{}')
    try:
        return json.loads(inventory_data_str)
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {inventory_data_str}", file=sys.stderr)
        return {}

if __name__ == "__main__":
    inventory = get_inventory()
    print(json.dumps(inventory))
