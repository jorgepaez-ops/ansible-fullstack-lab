# Ejercicio 02: Tu Primer Playbook

## Objetivo
Crear un playbook YAML que haga lo mismo que los comandos ad-hoc del ejercicio anterior,
pero de forma repetible y versionable.

## Concepto
Un **playbook** es un archivo YAML que define:
- **QUÉ** hacer (tareas/módulos)
- **DÓNDE** hacerlo (hosts)
- **CÓMO** hacerlo (parámetros, orden, privilegios)

Ventajas sobre ad-hoc:
- Repetible (mismo resultado cada vez)
- Versionable (git)
- Documentable (comentarios en YAML)
- Complejo (múltiples tareas en orden)

## Ejercicios

### 2.1 — Playbook mínimo
Ejecuta: `ansible-playbook ejercicios/02-playbook-basico/01-hola-mundo.yml`

### 2.2 — Múltiples tareas
Ejecuta: `ansible-playbook ejercicios/02-playbook-basico/02-multiples-tareas.yml`

### 2.3 — Múltiples plays
Ejecuta: `ansible-playbook ejercicios/02-playbook-basico/03-multiples-plays.yml`

### 2.4 — Check mode (dry-run)
```bash
# Ejecutar sin aplicar cambios (solo muestra qué haría)
ansible-playbook ejercicios/02-playbook-basico/02-multiples-tareas.yml --check

# Mostrar las diferencias (diff) que aplicaría
ansible-playbook ejercicios/02-playbook-basico/02-multiples-tareas.yml --check --diff
```

## Conceptos Aprendidos
- [ ] Estructura YAML de un playbook (---, name, hosts, tasks)
- [ ] Ejecución con ansible-playbook
- [ ] Múltiples tareas en un play
- [ ] Múltiples plays en un playbook
- [ ] Check mode (--check) y diff (--diff)
- [ ] Verbose mode (-v, -vv, -vvv)

## Siguiente
→ Ejercicio 03: Variables y Facts
