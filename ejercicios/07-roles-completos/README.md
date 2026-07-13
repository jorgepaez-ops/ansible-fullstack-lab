# Ejercicio 07: Roles Completos

## Objetivo
Crear un rol desde cero con estructura completa, entendiendo cada carpeta
y su función dentro de la jerarquía de Ansible.

## Concepto
Un **rol** es la forma estándar de organizar código Ansible reutilizable.
Encapsula tasks, handlers, templates, variables y metadatos en una estructura predecible.

## Estructura de un rol

```
roles/mi_rol/
├── tasks/main.yml        ← OBLIGATORIO: tareas a ejecutar
├── handlers/main.yml     ← Acciones reactivas (notify/listen)
├── templates/*.j2        ← Archivos Jinja2 (configuración dinámica)
├── files/*               ← Archivos estáticos (copiados tal cual)
├── vars/main.yml         ← Variables con ALTA prioridad (constantes del rol)
├── defaults/main.yml     ← Variables con BAJA prioridad (sobreescribibles)
├── meta/main.yml         ← Dependencias y metadatos (Galaxy)
└── README.md             ← Documentación del rol
```

## Ejercicios

### 7.1 — Crear un rol con ansible-galaxy init
```bash
# Crear esqueleto de un rol nuevo
ansible-galaxy role init ejercicios/07-roles-completos/roles/motd

# Ver la estructura generada
tree ejercicios/07-roles-completos/roles/motd
```

### 7.2 — Implementar el rol MOTD
El rol "motd" (Message Of The Day) configura el mensaje que aparece
al hacer login por SSH. Es un rol simple pero completo.

Archivos a crear/editar:
- `roles/motd/defaults/main.yml` — Variables por defecto
- `roles/motd/templates/motd.j2` — Template del mensaje
- `roles/motd/tasks/main.yml` — Tareas del rol
- `roles/motd/meta/main.yml` — Metadatos

### 7.3 — Ejecutar el rol
```bash
ansible-playbook ejercicios/07-roles-completos/playbook.yml
```

### 7.4 — Verificar el resultado
```bash
# Conectar por SSH y ver el MOTD
ssh -p 2221 root@127.0.0.1
# Deberías ver el mensaje personalizado
```

## Diferencias: defaults/ vs vars/
| Aspecto | defaults/ | vars/ |
|---------|-----------|-------|
| Prioridad | BAJA (se sobreescribe fácil) | ALTA (difícil de sobreescribir) |
| Uso | Valores configurables por el usuario | Constantes internas del rol |
| Ejemplo | `motd_hostname: "servidor"` | `motd_file_path: "/etc/motd"` |

## Conceptos Aprendidos
- [ ] ansible-galaxy role init (crear esqueleto)
- [ ] Estructura completa de un rol
- [ ] Diferencia entre defaults/ y vars/
- [ ] meta/main.yml y dependencias
- [ ] Cuándo crear un rol vs tasks inline

## Siguiente
→ Ejercicio 08: Ansible Vault (secretos)
