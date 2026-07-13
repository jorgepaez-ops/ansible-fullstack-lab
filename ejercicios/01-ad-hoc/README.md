# Ejercicio 01: Comandos Ad-Hoc

## Objetivo
Aprender a usar Ansible sin playbooks — directamente desde la terminal.

## Concepto
Un comando **ad-hoc** es una instrucción de Ansible que se ejecuta una sola vez,
sin necesidad de crear un archivo YAML. Es como usar `ssh` pero con superpoderes.

Formato:
```
ansible <hosts> -m <módulo> -a "<argumentos>"
```

## Prerequisitos
- Docker Compose corriendo: `docker compose up -d`
- Verificar conectividad: `ansible all -m ping`

## Ejercicios

### 1.1 — Ping (verificar conectividad)
```bash
# Ping a todos los hosts
ansible all -m ping

# Ping solo al grupo frontend
ansible frontend -m ping

# Ping a un host específico
ansible node1 -m ping
```

### 1.2 — Ejecutar comandos remotos
```bash
# Ver el hostname de cada nodo
ansible all -m ansible.builtin.command -a "hostname"

# Ver el espacio en disco
ansible all -m ansible.builtin.command -a "df -h"

# Ver los procesos corriendo
ansible all -m ansible.builtin.shell -a "ps aux | head -10"
```

> **Diferencia command vs shell:**
> - `command`: ejecuta directamente (NO soporta pipes |, redirecciones >, ni variables $)
> - `shell`: ejecuta a través de /bin/sh (SÍ soporta pipes y redirecciones)

### 1.3 — Gestión de paquetes
```bash
# Instalar un paquete en todos los nodos (requiere become)
ansible all -m ansible.builtin.apt -a "name=tree state=present" --become

# Verificar que se instaló
ansible all -m ansible.builtin.command -a "tree --version"

# Desinstalar el paquete
ansible all -m ansible.builtin.apt -a "name=tree state=absent" --become
```

### 1.4 — Gestión de archivos
```bash
# Crear un archivo en todos los nodos
ansible all -m ansible.builtin.copy -a "content='Hola desde Ansible\n' dest=/tmp/saludo.txt" --become

# Verificar que existe
ansible all -m ansible.builtin.command -a "cat /tmp/saludo.txt"

# Eliminar el archivo
ansible all -m ansible.builtin.file -a "path=/tmp/saludo.txt state=absent" --become
```

### 1.5 — Recolectar facts (información del sistema)
```bash
# Ver TODOS los facts de un host (es mucha info)
ansible node1 -m ansible.builtin.setup

# Filtrar solo facts de red
ansible node1 -m ansible.builtin.setup -a "filter=ansible_default_ipv4"

# Filtrar facts de memoria
ansible all -m ansible.builtin.setup -a "filter=ansible_memtotal_mb"

# Filtrar sistema operativo
ansible all -m ansible.builtin.setup -a "filter=ansible_distribution*"
```

### 1.6 — Paralelismo y límites
```bash
# Ejecutar en un solo host a la vez (serial)
ansible all -m ping --forks 1

# Limitar a un grupo
ansible webservers -m ping

# Limitar a un patrón
ansible 'node*' -m ping
```

## Conceptos Aprendidos
- [ ] Estructura de un comando ad-hoc
- [ ] Diferencia entre command y shell
- [ ] Módulos: ping, command, shell, apt, copy, file, setup
- [ ] Flags: --become, --forks, -m, -a
- [ ] Patrones de host: all, grupo, host, patrón*

## Siguiente
→ Ejercicio 02: Tu primer playbook
