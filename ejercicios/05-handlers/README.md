# Ejercicio 05: Handlers

## Objetivo
Entender cómo Ansible ejecuta acciones reactivas (solo cuando algo cambia).

## Concepto
Un **handler** es una tarea que SOLO se ejecuta si otra tarea la "notifica".

Flujo:
1. Tarea modifica un archivo de configuración → estado "changed"
2. La tarea tiene `notify: Nombre del Handler`
3. El handler se ENCOLA (no se ejecuta inmediatamente)
4. AL FINAL del play, TODOS los handlers encolados se ejecutan
5. Si la tarea no cambió nada (estado "ok") → el handler NO se ejecuta

## ¿Por qué importa?
Sin handlers, tendrías que reiniciar servicios SIEMPRE, incluso cuando nada cambió.
Con handlers, solo se reinicia si es necesario.

## Ejercicios

### 5.1 — Handlers básicos
```bash
ansible-playbook ejercicios/05-handlers/01-handlers-basicos.yml
```

### 5.2 — Ejecutar dos veces y observar la diferencia
```bash
# Primera vez: todo se ejecuta (changed) → handlers se ejecutan
ansible-playbook ejercicios/05-handlers/01-handlers-basicos.yml

# Segunda vez: nada cambió (ok) → handlers NO se ejecutan
ansible-playbook ejercicios/05-handlers/01-handlers-basicos.yml
```

## Conceptos Aprendidos
- [ ] notify: para encolar handlers
- [ ] handlers: sección del play
- [ ] Handlers solo se ejecutan con estado "changed"
- [ ] Handlers se ejecutan al FINAL del play (no inmediatamente)
- [ ] meta: flush_handlers para forzar ejecución inmediata
- [ ] listen: para agrupar handlers bajo un evento

## Siguiente
→ Ejercicio 06: Templates Jinja2
