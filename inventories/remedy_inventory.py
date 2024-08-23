#!/usr/bin/env python3
import json
import sys
import os

def get_inventory():
    # In AAP, this data will be provided by the workflow
    inventory_data = json.loads(os.environ.get('INVENTORY_DATA', '{}'))
    
    # Process the inventory data
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
