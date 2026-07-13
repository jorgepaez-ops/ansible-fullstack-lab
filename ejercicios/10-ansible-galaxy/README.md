# Ejercicio 10: Ansible Galaxy

## Objetivo
Aprender a usar Ansible Galaxy para instalar roles y collections de la comunidad,
y preparar tus propios roles para compartir.

## Concepto
**Ansible Galaxy** es el repositorio público de roles y collections.
Es como npm para Node.js o pip para Python, pero para Ansible.

- URL: https://galaxy.ansible.com
- Roles: paquetes de tareas reutilizables creados por la comunidad
- Collections: paquetes que incluyen roles + módulos + plugins

## Comandos principales

```bash
# ─────────────────────────────────────────────────────────────────────
# COLLECTIONS (paquetes con módulos, roles y plugins)
# ─────────────────────────────────────────────────────────────────────

# Instalar una collection específica
ansible-galaxy collection install community.postgresql

# Instalar desde requirements.yml (recomendado)
ansible-galaxy collection install -r requirements.yml

# Ver collections instaladas
ansible-galaxy collection list

# ─────────────────────────────────────────────────────────────────────
# ROLES (paquetes de tareas reutilizables)
# ─────────────────────────────────────────────────────────────────────

# Buscar roles populares
ansible-galaxy search nginx
ansible-galaxy search --author geerlingguy

# Instalar un rol de Galaxy
ansible-galaxy role install geerlingguy.docker
ansible-galaxy role install geerlingguy.nginx

# Instalar roles desde requirements.yml
ansible-galaxy role install -r requirements.yml

# Ver roles instalados
ansible-galaxy role list

# Crear esqueleto para un nuevo rol
ansible-galaxy role init mi_nuevo_rol
```

## Ejercicios

### 10.1 — Instalar collections del proyecto
```bash
# Instalar todas las collections declaradas en requirements.yml
ansible-galaxy collection install -r requirements.yml

# Verificar que se instalaron
ansible-galaxy collection list | grep -E "postgresql|general|posix"
```

### 10.2 — Instalar un rol popular de la comunidad
```bash
# Instalar rol de Docker por geerlingguy (uno de los más populares)
ansible-galaxy role install geerlingguy.docker

# Ver dónde se instaló
ansible-galaxy role list

# Explorar su estructura
ls ~/.ansible/roles/geerlingguy.docker/
```

### 10.3 — Usar un rol de Galaxy en un playbook
```bash
ansible-playbook ejercicios/10-ansible-galaxy/playbook.yml
```

### 10.4 — Crear requirements.yml con roles y collections
```bash
# Ver el archivo de ejemplo
cat ejercicios/10-ansible-galaxy/requirements.yml

# Instalar todo de una vez
ansible-galaxy install -r ejercicios/10-ansible-galaxy/requirements.yml
```

### 10.5 — Crear tu propio rol publicable
```bash
# Crear esqueleto con metadata de Galaxy
ansible-galaxy role init --init-path ./roles mi_rol_publicable

# Estructura creada:
# mi_rol_publicable/
# ├── README.md        ← Documentación (obligatoria para Galaxy)
# ├── defaults/main.yml
# ├── handlers/main.yml
# ├── meta/main.yml    ← Metadatos de Galaxy
# ├── tasks/main.yml
# ├── templates/
# ├── tests/           ← Tests del rol
# └── vars/main.yml
```

## Roles populares recomendados

| Autor | Rol | Descripción |
|-------|-----|-------------|
| geerlingguy | docker | Instala Docker CE |
| geerlingguy | nginx | Configura Nginx |
| geerlingguy | postgresql | PostgreSQL server |
| geerlingguy | certbot | Certificados SSL Let's Encrypt |
| geerlingguy | java | Instala Java/OpenJDK |
| oefenweb | fail2ban | Protección contra brute-force |

## Buenas Prácticas
1. Siempre declara dependencias en `requirements.yml`
2. Fija versiones específicas (evita romper builds futuros)
3. Prefiere collections oficiales sobre roles sueltos
4. Lee el README del rol antes de usarlo (entiende las variables)
5. En CI/CD: `ansible-galaxy install -r requirements.yml` como primer paso

## Conceptos Aprendidos
- [ ] ansible-galaxy collection install
- [ ] ansible-galaxy role install
- [ ] requirements.yml para declarar dependencias
- [ ] Explorar Galaxy (galaxy.ansible.com)
- [ ] Crear esqueleto con ansible-galaxy role init
- [ ] Namespace en collections (community.postgresql.postgresql_db)

## Fin del Curso de Ejercicios
Has completado los 10 ejercicios. Ahora aplica todo lo aprendido
en el proyecto principal (los 3 roles del fullstack lab).
