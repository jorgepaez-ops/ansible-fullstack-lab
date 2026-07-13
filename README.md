# Ansible Fullstack Lab

Laboratorio de aprendizaje de Ansible con un stack completo:
**Nginx + Spring Boot + PostgreSQL**, orquestado con Docker Compose
y automatizado con Ansible.

## Arquitectura del Lab

```
┌─────────────────────────────────────────────────────────┐
│  Tu Mac (Control Node)                                   │
│  ansible-playbook playbook.yml                           │
│                                                          │
│    SSH :2221        SSH :2222         SSH :2223           │
│      │                │                  │               │
│      ▼                ▼                  ▼               │
│  ┌────────┐     ┌──────────┐     ┌────────────┐        │
│  │ node1  │     │  node2   │     │   node3    │        │
│  │ Nginx  │────▶│  Spring  │────▶│ PostgreSQL │        │
│  │ :80    │     │  Boot    │     │ :5432      │        │
│  │        │     │  :8080   │     │            │        │
│  └────────┘     └──────────┘     └────────────┘        │
│   Frontend        Backend          Database              │
│   Host :8081     Host :8080       Host :5432             │
└─────────────────────────────────────────────────────────┘
```

Los 3 nodos son contenedores Docker con Ubuntu 24.04 + SSH,
simulando servidores reales que Ansible gestiona por SSH.

---

## Setup en macOS (desde cero)

### Paso 1: Instalar Homebrew (si no lo tienes)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Paso 2: Instalar Python y pipx

```bash
# Python 3 (macOS ya lo incluye, pero Homebrew da una versión más reciente)
brew install python@3.12

# pipx: instala herramientas Python en entornos aislados
brew install pipx
pipx ensurepath
```

### Paso 3: Instalar Ansible

```bash
# Instalar Ansible via pipx (aislado del sistema)
pipx install ansible --include-deps

# Verificar instalación
ansible --version
# Debe mostrar: ansible [core 2.17.x] o superior

# Instalar linter (opcional pero recomendado)
pipx install ansible-lint
```

### Paso 4: Instalar Docker Desktop

```bash
brew install --cask docker
# Abrir Docker Desktop y aceptar términos
open -a Docker
```

### Paso 5: Generar SSH Key para el lab

```bash
# Crear key dedicada (sin passphrase para el lab)
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_ansible -N ""

# Verificar que existe
ls -la ~/.ssh/id_rsa_ansible*
```

### Paso 6: Instalar Collections de Ansible

```bash
# Desde el directorio del proyecto
cd ~/Documents/Proyectos/ansible-fullstack-lab
ansible-galaxy collection install -r requirements.yml
```

### Paso 7: Levantar el Lab

```bash
# Construir y levantar los 3 contenedores
docker compose up -d --build

# Verificar que están corriendo
docker compose ps
```

### Paso 8: Copiar SSH Key a los contenedores

```bash
# Copiar la key pública a cada nodo (password: root)
ssh-copy-id -i ~/.ssh/id_rsa_ansible -p 2221 root@127.0.0.1
ssh-copy-id -i ~/.ssh/id_rsa_ansible -p 2222 root@127.0.0.1
ssh-copy-id -i ~/.ssh/id_rsa_ansible -p 2223 root@127.0.0.1
```

### Paso 9: Verificar conectividad

```bash
ansible all -m ping
# Esperado: SUCCESS para los 3 nodos
```

### Paso 10: Ejecutar el playbook principal

```bash
ansible-playbook playbook.yml
```

---

## Estructura del Proyecto

```
ansible-fullstack-lab/
├── ansible.cfg                 # Configuración global de Ansible
├── inventory.ini               # Inventario de hosts (3 nodos Docker)
├── requirements.yml            # Collections externas necesarias
├── playbook.yml                # Playbook principal (orquesta los 3 roles)
├── .ansible-lint               # Configuración del linter
│
├── group_vars/                 # Variables por grupo de hosts
│   ├── all.yml                 #   → Variables globales
│   ├── frontend.yml            #   → Config de Nginx
│   ├── backend.yml             #   → Config de Spring Boot
│   └── database.yml            #   → Config de PostgreSQL
│
├── roles/                      # Roles (lógica modular)
│   ├── frontend/               #   → Nginx: install, config, deploy
│   │   ├── tasks/main.yml
│   │   ├── handlers/main.yml
│   │   ├── templates/nginx.conf.j2
│   │   ├── defaults/main.yml
│   │   └── meta/main.yml
│   ├── backend/                #   → Spring Boot: java, jar, systemd
│   │   ├── tasks/main.yml
│   │   ├── handlers/main.yml
│   │   ├── templates/app.service.j2
│   │   ├── templates/app.env.j2
│   │   ├── defaults/main.yml
│   │   └── meta/main.yml
│   └── database/               #   → PostgreSQL: install, users, dbs
│       ├── tasks/main.yml
│       ├── handlers/main.yml
│       ├── defaults/main.yml
│       └── meta/main.yml
│
├── files/                      # Archivos estáticos desplegados por roles
│   ├── index.html              #   → Página web del frontend
│   ├── init.sql                #   → Script SQL inicial
│   └── README.md
│
├── ejercicios/                 # 10 ejercicios progresivos
│   ├── 01-ad-hoc/             #   → Comandos sin playbook
│   ├── 02-playbook-basico/    #   → Tu primer playbook
│   ├── 03-variables-y-facts/  #   → Variables + info del sistema
│   ├── 04-condicionales-y-loops/ # → when: y loop:
│   ├── 05-handlers/           #   → Acciones reactivas
│   ├── 06-templates-jinja2/   #   → Archivos dinámicos
│   ├── 07-roles-completos/    #   → Crear un rol desde cero
│   ├── 08-vault-secretos/     #   → Cifrar contraseñas
│   ├── 09-inventarios-dinamicos/ # → Descubrir hosts automáticamente
│   └── 10-ansible-galaxy/     #   → Usar roles de la comunidad
│
├── docker-compose.yml          # Infraestructura local (3 contenedores)
├── Dockerfile.ubuntu           # Imagen base con SSH
└── .gitignore
```

---

## Comandos Frecuentes

### Gestión del Lab (Docker)

```bash
# Levantar todo
docker compose up -d

# Ver estado
docker compose ps

# Ver logs de un nodo
docker compose logs node1

# Entrar a un contenedor
docker exec -it node1 bash

# Reconstruir (si cambias Dockerfile)
docker compose build --no-cache

# Detener todo
docker compose down

# Detener y eliminar volúmenes (reset completo)
docker compose down -v
```

### Ansible — Ejecución

```bash
# Playbook completo
ansible-playbook playbook.yml

# Solo un grupo de hosts
ansible-playbook playbook.yml --limit frontend

# Solo tareas con cierto tag
ansible-playbook playbook.yml --tags "deploy"
ansible-playbook playbook.yml --tags "database-config"

# Dry-run (muestra qué haría sin ejecutar)
ansible-playbook playbook.yml --check --diff

# Verbose (más detalle)
ansible-playbook playbook.yml -v     # mínimo
ansible-playbook playbook.yml -vvv   # máximo
```

### Ansible — Información

```bash
# Verificar conectividad
ansible all -m ping

# Ver inventario como árbol
ansible-inventory --graph

# Ver facts de un host
ansible node1 -m setup

# Ver facts filtrados
ansible node1 -m setup -a "filter=ansible_distribution*"

# Listar tags disponibles
ansible-playbook playbook.yml --list-tags

# Listar tareas que se ejecutarían
ansible-playbook playbook.yml --list-tasks
```

### Ansible — Vault (secretos)

```bash
# Crear archivo cifrado
ansible-vault create secretos.yml

# Editar archivo cifrado
ansible-vault edit secretos.yml

# Ver sin descifrar permanentemente
ansible-vault view secretos.yml

# Ejecutar playbook con secretos
ansible-playbook playbook.yml --ask-vault-pass
```

### Ansible — Galaxy (dependencias)

```bash
# Instalar collections
ansible-galaxy collection install -r requirements.yml

# Instalar roles
ansible-galaxy role install geerlingguy.docker

# Crear esqueleto de rol nuevo
ansible-galaxy role init roles/mi_nuevo_rol
```

---

## Ejercicios Progresivos

Los ejercicios están diseñados para completarse en orden.
Cada uno introduce un concepto nuevo y construye sobre el anterior.

| # | Tema | Concepto clave |
|---|------|----------------|
| 01 | Ad-hoc | Comandos Ansible sin playbook |
| 02 | Playbook básico | Estructura YAML, plays, tasks |
| 03 | Variables y Facts | Parametrización y datos del sistema |
| 04 | Condicionales y Loops | Control de flujo (when, loop) |
| 05 | Handlers | Acciones reactivas (notify/listen) |
| 06 | Templates Jinja2 | Archivos de configuración dinámicos |
| 07 | Roles completos | Modularización y reutilización |
| 08 | Vault | Gestión segura de secretos |
| 09 | Inventarios dinámicos | Descubrimiento automático de hosts |
| 10 | Galaxy | Ecosistema y dependencias externas |

```bash
# Ejemplo: ejecutar ejercicio 02
ansible-playbook ejercicios/02-playbook-basico/01-hola-mundo.yml
```

---

## Preparación para Certificación

Este lab cubre los temas del examen **Red Hat EX294** (RHCE - Ansible):

- [x] Instalar y configurar Ansible
- [x] Crear inventarios estáticos y dinámicos
- [x] Escribir playbooks con múltiples plays
- [x] Variables, facts y precedencia
- [x] Condicionales y loops
- [x] Handlers
- [x] Templates Jinja2
- [x] Roles (crear y usar)
- [x] Ansible Vault
- [x] Ansible Galaxy (roles y collections)
- [x] Tags para ejecución selectiva
- [x] Gestión de servicios (systemd)
- [x] Gestión de paquetes (apt)
- [x] Gestión de archivos y permisos
- [x] FQCN (Fully Qualified Collection Names)

---

## Versiones Utilizadas

| Componente | Versión |
|------------|---------|
| Ansible | 9.x (core 2.17+) |
| Python | 3.12+ |
| Docker | 24+ |
| Ubuntu (contenedores) | 24.04 LTS |
| PostgreSQL | 16 |
| Java | OpenJDK 21 |
| Nginx | Latest (apt) |

---

## Troubleshooting

### "Permission denied" al conectar por SSH
```bash
# Verificar que la key existe
ls ~/.ssh/id_rsa_ansible

# Re-copiar la key al contenedor
ssh-copy-id -i ~/.ssh/id_rsa_ansible -p 2221 root@127.0.0.1
```

### "Host key verification failed"
```bash
# Limpiar known_hosts (normal después de recrear contenedores)
ssh-keygen -R "[127.0.0.1]:2221"
ssh-keygen -R "[127.0.0.1]:2222"
ssh-keygen -R "[127.0.0.1]:2223"
```

### Contenedores no arrancan
```bash
# Ver si hay conflicto de puertos
docker compose logs
lsof -i :2221  # Ver qué usa el puerto

# Reconstruir desde cero
docker compose down -v
docker compose up -d --build
```

### Collection no encontrada
```bash
# Instalar collections
ansible-galaxy collection install -r requirements.yml --force
```

---

## Recursos de Aprendizaje

- [Documentación oficial de Ansible](https://docs.ansible.com/)
- [Ansible for DevOps (libro gratuito)](https://www.ansiblefordevops.com/)
- [RHCE EX294 Objectives](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux-9)
- [Ansible Galaxy](https://galaxy.ansible.com/)
- [Ansible Lint](https://ansible.readthedocs.io/projects/lint/)
