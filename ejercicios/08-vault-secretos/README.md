# Ejercicio 08: Ansible Vault (Secretos)

## Objetivo
Aprender a cifrar y gestionar secretos (contraseñas, API keys, certificados)
de forma segura con Ansible Vault.

## Concepto
**Ansible Vault** cifra archivos o variables individuales con AES-256.
Esto permite guardar secretos en git de forma segura — solo quien tiene
la contraseña de vault puede descifrarlos.

## Comandos principales

```bash
# Crear un archivo cifrado desde cero
ansible-vault create secretos.yml

# Cifrar un archivo existente
ansible-vault encrypt archivo.yml

# Descifrar un archivo (dejarlo en texto plano)
ansible-vault decrypt archivo.yml

# Ver contenido sin descifrar permanentemente
ansible-vault view secretos.yml

# Editar un archivo cifrado (descifra → editor → recifra)
ansible-vault edit secretos.yml

# Cifrar una sola variable (inline)
ansible-vault encrypt_string 'mi_secreto' --name 'db_password'
```

## Ejercicios

### 8.1 — Crear archivo de secretos
```bash
# Crear archivo cifrado (te pedirá contraseña de vault)
# Usa "lab123" como contraseña para este ejercicio
ansible-vault create ejercicios/08-vault-secretos/vars/secretos.yml
```

Contenido sugerido para el archivo:
```yaml
db_password: "super_secreto_123"
api_key: "sk-abc123xyz789"
ssl_private_key: |
  -----BEGIN PRIVATE KEY-----
  MIIEvgIBADANBgkqhkiG9w0BAQ...
  -----END PRIVATE KEY-----
```

### 8.2 — Usar secretos en un playbook
```bash
# Ejecutar playbook que usa secretos (pide password interactivamente)
ansible-playbook ejercicios/08-vault-secretos/playbook.yml --ask-vault-pass

# Ejecutar usando archivo de password (para CI/CD)
ansible-playbook ejercicios/08-vault-secretos/playbook.yml --vault-password-file .vault_pass
```

### 8.3 — Cifrar variable individual
```bash
# Cifrar un string y obtener la versión para pegar en YAML
ansible-vault encrypt_string 'mi_password_segura' --name 'pg_password'

# El output se pega directo en group_vars/database.yml:
# pg_password: !vault |
#   $ANSIBLE_VAULT;1.1;AES256
#   6163616...
```

### 8.4 — Vault password file (para automatización)
```bash
# Crear archivo con la contraseña (NO commitear a git)
echo "lab123" > .vault_pass
chmod 600 .vault_pass

# Agregar a .gitignore
echo ".vault_pass" >> .gitignore

# Configurar en ansible.cfg para no tener que pasarlo siempre
# vault_password_file = .vault_pass
```

## Buenas Prácticas
1. NUNCA commitees `.vault_pass` a git
2. Usa nombres claros: `vault_db_password` (prefijo vault_)
3. Un vault password por entorno (dev, staging, prod)
4. En CI/CD: password como variable de entorno o secret manager
5. Rota los passwords de vault periódicamente

## Conceptos Aprendidos
- [ ] ansible-vault create/encrypt/decrypt/edit/view
- [ ] --ask-vault-pass vs --vault-password-file
- [ ] encrypt_string para variables inline
- [ ] Separación de secretos en archivos dedicados
- [ ] Vault IDs para múltiples passwords

## Siguiente
→ Ejercicio 09: Inventarios dinámicos
