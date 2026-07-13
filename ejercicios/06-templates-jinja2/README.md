# Ejercicio 06: Templates Jinja2

## Objetivo
Generar archivos de configuración dinámicos usando plantillas con variables,
condicionales y bucles integrados.

## Concepto
Una **plantilla Jinja2** (.j2) es un archivo con "huecos" que Ansible rellena
con variables al copiarlo al servidor destino.

Sintaxis:
- `{{ variable }}` → Interpola el valor
- `{% if condicion %}...{% endif %}` → Bloque condicional
- `{% for item in lista %}...{% endfor %}` → Bucle
- `{# comentario #}` → Comentario (no aparece en el archivo final)
- `{{ variable | filtro }}` → Aplica un filtro (transformación)

## Ejercicios

### 6.1 — Template básico con variables
```bash
ansible-playbook ejercicios/06-templates-jinja2/01-template-basico.yml
```

### 6.2 — Template con condicionales y loops
```bash
ansible-playbook ejercicios/06-templates-jinja2/02-template-avanzado.yml
```

## Filtros Jinja2 más útiles
- `{{ var | default("valor") }}` — Valor por defecto si no existe
- `{{ var | upper }}` — Convertir a mayúsculas
- `{{ var | lower }}` — Convertir a minúsculas
- `{{ lista | join(", ") }}` — Unir lista en string
- `{{ var | int }}` — Convertir a entero
- `{{ var | to_yaml }}` — Convertir a YAML
- `{{ var | regex_replace("patrón", "reemplazo") }}` — Regex

## Conceptos Aprendidos
- [ ] Módulo ansible.builtin.template vs ansible.builtin.copy
- [ ] Sintaxis {{ }}, {% %}, {# #}
- [ ] Filtros Jinja2 (default, upper, join, etc.)
- [ ] Condicionales y loops dentro de templates
- [ ] validate: para verificar sintaxis antes de aplicar

## Siguiente
→ Ejercicio 07: Roles completos
