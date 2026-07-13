-- =============================================================================
-- files/init.sql — Script de inicialización de la base de datos
-- =============================================================================
--
-- PROPÓSITO:
--   Crear la estructura inicial de tablas y datos de ejemplo.
--   Este script se ejecuta UNA VEZ al configurar PostgreSQL por primera vez.
--
-- EJECUTADO POR:
--   El rol database (roles/database/tasks/main.yml) usando el módulo
--   community.postgresql.postgresql_script
--
-- IDEMPOTENCIA:
--   Usamos "IF NOT EXISTS" para que el script no falle si se ejecuta
--   más de una vez (aunque Ansible lo controla con `when: changed`).
--
-- BASE DE DATOS:
--   Se ejecuta contra: messagesdb (definida en group_vars/database.yml)
-- =============================================================================

-- ─────────────────────────────────────────────────────────────────────────────
-- Tabla: messages
-- ─────────────────────────────────────────────────────────────────────────────
-- Almacena mensajes simples. El backend Spring Boot consume esta tabla.
-- Estructura minimalista para el laboratorio.
CREATE TABLE IF NOT EXISTS messages (
    id          SERIAL PRIMARY KEY,          -- Auto-incremento (equivale a IDENTITY en otros RDBMS)
    content     VARCHAR(500) NOT NULL,       -- Contenido del mensaje
    author      VARCHAR(100) DEFAULT 'anonymous',  -- Autor (opcional)
    created_at  TIMESTAMP DEFAULT NOW()      -- Fecha de creación automática
);

-- ─────────────────────────────────────────────────────────────────────────────
-- Datos de ejemplo (seed data)
-- ─────────────────────────────────────────────────────────────────────────────
-- ON CONFLICT DO NOTHING evita errores si los datos ya existen.
-- Esto hace el INSERT idempotente (seguro de ejecutar múltiples veces).
INSERT INTO messages (id, content, author) VALUES
    (1, 'Hola desde PostgreSQL, desplegado con Ansible', 'admin'),
    (2, 'Este mensaje fue insertado por el script init.sql', 'sistema'),
    (3, 'El stack completo funciona: Nginx + Spring Boot + PostgreSQL', 'lab')
ON CONFLICT (id) DO NOTHING;

-- ─────────────────────────────────────────────────────────────────────────────
-- Índice para búsquedas por autor (ejemplo de optimización básica)
-- ─────────────────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_messages_author ON messages(author);

-- ─────────────────────────────────────────────────────────────────────────────
-- Verificación final
-- ─────────────────────────────────────────────────────────────────────────────
-- Imprime el conteo de registros para confirmar que la inserción funcionó.
-- Visible en los logs de Ansible cuando ejecuta el script.
SELECT COUNT(*) AS total_messages FROM messages;
