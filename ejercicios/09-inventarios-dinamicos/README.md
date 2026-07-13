# Ejercicio 09: Inventarios Dinámicos

## Objetivo
Entender cómo Ansible puede descubrir hosts automáticamente desde
fuentes externas (AWS, Docker, scripts custom) en vez de listarlos manualmente.

## Concepto
Un **inventario dinámico** es un script o plugin que genera la lista de hosts
en tiempo real consultando una fuente externa.

### Inventario Estático vs Dinámico
| Aspecto | Estático (.ini/.yml) | Dinámico (plugin/script) |
|---------|---------------------|--------------------------|
| Hosts | Definidos manualmente | Descubiertos automáticamente |
| Escalabilidad | Manual (agregar a mano) | Automática |
| Actualización | Editar archivo | Re-ejecutar query |
| Uso típico | Labs, entornos fijos | Cloud, contenedores |

## Inventarios Dinámicos Comunes
- `amazon.aws.aws_ec2` — Descubre instancias EC2
- `azure.azcollection.azure_rm` — Descubre VMs en Azure
- `google.cloud.gcp_compute` — Instancias en GCP
- `community.docker.docker_containers` — Contenedores Docker
- `Script custom` — Cualquier fuente (API, CMDB, etc.)

## Ejercicios

### 9.1 — Inventario dinámico de Docker
```bash
# Ver hosts descubiertos automáticamente
ansible-inventory -i ejercicios/09-inventarios-dinamicos/docker.yml --list

# Ping a contenedores descubiertos
ansible all -i ejercicios/09-inventarios-dinamicos/docker.yml -m ping
```

### 9.2 — Script de inventario custom
```bash
# Ver output del script
python3 ejercicios/09-inventarios-dinamicos/custom_inventory.py --list

# Usar como inventario
ansible all -i ejercicios/09-inventarios-dinamicos/custom_inventory.py -m ping
```

### 9.3 — Combinar inventarios
```bash
# Ansible puede usar un DIRECTORIO como inventario
# Combina todos los archivos dentro (estáticos + dinámicos)
ansible-inventory -i ejercicios/09-inventarios-dinamicos/inventories/ --graph
```

## Formato de un Inventario Dinámico (JSON)
Un script debe retornar JSON con esta estructura:
```json
{
  "grupo1": {
    "hosts": ["host1", "host2"],
    "vars": { "variable": "valor" }
  },
  "grupo2": {
    "hosts": ["host3"]
  },
  "_meta": {
    "hostvars": {
      "host1": { "ansible_host": "10.0.0.1" }
    }
  }
}
```

## Conceptos Aprendidos
- [ ] Diferencia inventario estático vs dinámico
- [ ] Plugin de inventario (YAML config)
- [ ] Script de inventario (Python/Bash que retorna JSON)
- [ ] Combinar múltiples fuentes en un directorio
- [ ] ansible-inventory --list / --graph

## Siguiente
→ Ejercicio 10: Ansible Galaxy
