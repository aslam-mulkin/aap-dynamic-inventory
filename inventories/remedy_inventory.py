---
- name: Update Dynamic Inventory
  hosts: localhost
  connection: local
  gather_facts: no
  
  vars:
    inventory_data: "{{ api_inventory_data | default({}) }}"

  tasks:
    - name: Display inventory data
      debug:
        var: inventory_data

    - name: Update inventory source configuration
      ansible.controller.inventory_source:
        name: "Inventory from Remedy API"
        inventory: "Dynamic Inventory from Remedy"
        organization: "Default"
        source: "scm"
        source_project: "Hardening"  # Replace with your project name
        source_path: "inventories/remedy_inventory.py"
        update_on_launch: true
        overwrite: true
        source_vars:
          INVENTORY_DATA: "{{ inventory_data | to_json }}"
      register: inventory_source_update

    - name: Display inventory source update result
      debug:
        var: inventory_source_update

    - name: Trigger inventory update
      ansible.controller.inventory_source_update:
        name: "Inventory from Remedy API"
        inventory: "Dynamic Inventory from Remedy"
        organization: "Default"
      register: inventory_update_result

    - name: Wait for inventory update
      ansible.controller.job_wait:
        job_id: "{{ inventory_update_result.id }}"
      register: wait_result
      when: inventory_update_result is success

    - name: Display wait result
      debug:
        var: wait_result

    - name: Display updated inventory
      debug:
        msg: "Updated inventory: {{ lookup('ansible.controller.controller_api', 'inventories/' + inventory_update_result.id + '/hosts') }}"
