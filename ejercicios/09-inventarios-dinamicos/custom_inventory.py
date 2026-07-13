#!/usr/bin/env python3
# =============================================================================
# ejercicios/09-inventarios-dinamicos/custom_inventory.py
# =============================================================================
#
# SCRIPT DE INVENTARIO DINÁMICO PERSONALIZADO
#
# Un script de inventario dinámico es un programa que Ansible ejecuta
# y cuyo output (JSON en stdout) define los hosts y grupos.
#
# REQUISITOS DEL SCRIPT:
#   1. Debe ser ejecutable (chmod +x)
#   2. Debe aceptar --list (retorna inventario completo)
#   3. Debe aceptar --host <nombre> (retorna vars de un host)
#   4. Output: JSON válido en stdout
#
# USO:
#   chmod +x ejercicios/09-inventarios-dinamicos/custom_inventory.py
#   ansible-inventory -i ejercicios/09-inventarios-dinamicos/custom_inventory.py --list
#   ansible all -i ejercicios/09-inventarios-dinamicos/custom_inventory.py -m ping
#
# EN LA VIDA REAL:
#   Aquí consultarías una API (AWS, CMDB, base de datos) para descubrir hosts.
#   Este ejemplo simula la respuesta para fines didácticos.
# =============================================================================

import json
import sys


def get_inventory():
    """
    Retorna el inventario completo.
    En un caso real, aquí harías llamadas a APIs:
      - boto3 para AWS
      - requests para una API REST
      - psycopg2 para una base de datos
    """
    inventory = {
        # Grupo: frontend
        "frontend": {
            "hosts": ["node1"],
            "vars": {
                "nginx_port": 80
            }
        },
        # Grupo: backend
        "backend": {
            "hosts": ["node2"],
            "vars": {
                "app_port": 8080
            }
        },
        # Grupo: database
        "database": {
            "hosts": ["node3"],
            "vars": {
                "pg_port": 5432
            }
        },
        # Grupo padre que agrupa frontend + backend
        "webservers": {
            "children": ["frontend", "backend"]
        },
        # _meta: variables específicas por host
        # Esto evita que Ansible llame --host para cada host individualmente
        "_meta": {
            "hostvars": {
                "node1": {
                    "ansible_host": "127.0.0.1",
                    "ansible_port": 2221,
                    "ansible_user": "root",
                    "ansible_ssh_private_key_file": "~/.ssh/id_rsa_ansible"
                },
                "node2": {
                    "ansible_host": "127.0.0.1",
                    "ansible_port": 2222,
                    "ansible_user": "root",
                    "ansible_ssh_private_key_file": "~/.ssh/id_rsa_ansible"
                },
                "node3": {
                    "ansible_host": "127.0.0.1",
                    "ansible_port": 2223,
                    "ansible_user": "root",
                    "ansible_ssh_private_key_file": "~/.ssh/id_rsa_ansible"
                }
            }
        }
    }
    return inventory


def get_host_vars(hostname):
    """Retorna variables de un host específico (llamado con --host)."""
    inventory = get_inventory()
    return inventory["_meta"]["hostvars"].get(hostname, {})


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--list":
        # Retornar inventario completo
        print(json.dumps(get_inventory(), indent=2))
    elif len(sys.argv) == 3 and sys.argv[1] == "--host":
        # Retornar variables de un host específico
        print(json.dumps(get_host_vars(sys.argv[2]), indent=2))
    else:
        print(json.dumps({"_meta": {"hostvars": {}}}))

    sys.exit(0)
