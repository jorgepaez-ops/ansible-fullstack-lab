# Ejercicio 03: Variables y Facts

## Objetivo
Entender cómo Ansible gestiona datos dinámicos: variables definidas por ti
y facts recolectados del sistema.

## Conceptos

### Variables
Datos que defines TÚ y que Ansible usa para parametrizar las tareas.
Se definen en múltiples lugares (orden de prioridad ascendente):
1. `roles/defaults/main.yml` (menor prioridad)
2. `group_vars/*.yml`
3. `host_vars/*.yml`
4. `vars:` en el play
5. `vars_files:` importados
6. `-e` / `--extra-vars` en CLI (máxima prioridad)

### Facts
Datos que Ansible **descubre automáticamente** sobre cada host:
- Sistema operativo, versión, kernel
- RAM, CPUs, disco
- Interfaces de red, IPs
- Variables de entorno

Se acceden como `ansible_*` (ej: `ansible_distribution`)

## Ejercicios

### 3.1 — Variables inline y precedencia
```bash
ansible-playbook ejercicios/03-variables-y-facts/01-variables.yml
```

### 3.2 — Facts del sistema
```bash
ansible-playbook ejercicios/03-variables-y-facts/02-facts.yml
```

### 3.3 — Extra vars desde CLI (máxima prioridad)
```bash
ansible-playbook ejercicios/03-variables-y-facts/01-variables.yml -e "app_name=ProductionApp app_port=9090"
```

## Conceptos Aprendidos
- [ ] vars: en un play
- [ ] vars_files: para separar variables
- [ ] Jerarquía de precedencia
- [ ] ansible_facts y gather_facts
- [ ] register: para capturar output
- [ ] -e / --extra-vars para override

## Siguiente
→ Ejercicio 04: Condicionales y Loops
