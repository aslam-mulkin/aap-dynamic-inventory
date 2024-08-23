#!/usr/bin/env python3
import json
import sys
import os
from jinja2 import Template

def get_inventory():
    inventory_data_str = os.environ.get('INVENTORY_DATA', '{}')
    
    # Handle potential Jinja2 template string
    if '{{' in inventory_data_str and '}}' in inventory_data_str:
        inventory_data_str = Template(inventory_data_str).render(source_vars={})
    
    try:
        return json.loads(inventory_data_str)
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {inventory_data_str}", file=sys.stderr)
        return {"all": {"children": {}}}

if __name__ == "__main__":
    inventory = get_inventory()
    print(json.dumps(inventory))
