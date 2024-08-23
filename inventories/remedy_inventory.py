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

    processed_inventory = {
        "_meta": {"hostvars": {}},
        "all": {"children": []}
    }
    
    for group, group_data in inventory_data.get('all', {}).get('children', {}).items():
        processed_inventory[group] = {"hosts": group_data.get('hosts', [])}
        processed_inventory["all"]["children"].append(group)
        for host in group_data.get('hosts', []):
            processed_inventory["_meta"]["hostvars"][host] = {"group": group}
    
    return processed_inventory

if __name__ == "__main__":
    inventory = get_inventory()
    print(json.dumps(inventory))
