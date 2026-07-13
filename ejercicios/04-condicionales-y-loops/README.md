# Ejercicio 04: Condicionales y Loops

## Objetivo
Controlar el flujo de ejecución: ejecutar tareas condicionalmente y repetir
acciones sobre listas de elementos.

## Conceptos

### when: (condicional)
Ejecuta una tarea SOLO si la condición es verdadera.
Usa expresiones Jinja2 (Python-like): `==`, `!=`, `>`, `<`, `in`, `not`, `and`, `or`

```yaml
- name: Solo en Ubuntu
  ansible.builtin.apt: ...
  when: ansible_distribution == "Ubuntu"
```

### loop: (bucle)
Repite una tarea para cada elemento de una lista.
El elemento actual se accede con `{{ item }}`.

```yaml
- name: Instalar múltiples paquetes
  ansible.builtin.apt:
    name: "{{ item }}"
    state: present
  loop:
    - vim
    - curl
    - htop
```

## Ejercicios

### 4.1 — Condicionales básicos
```bash
ansible-playbook ejercicios/04-condicionales-y-loops/01-condicionales.yml
```

### 4.2 — Loops básicos
```bash
ansible-playbook ejercicios/04-condicionales-y-loops/02-loops.yml
```

## Conceptos Aprendidos
- [ ] when: con comparaciones (==, !=, >, <)
- [ ] when: con operadores lógicos (and, or, not)
- [ ] when: con facts (ansible_distribution, etc.)
- [ ] when: con register (resultado de tarea anterior)
- [ ] loop: con lista simple
- [ ] loop: con lista de diccionarios
- [ ] Combinar when + loop

## Siguiente
→ Ejercicio 05: Handlers
