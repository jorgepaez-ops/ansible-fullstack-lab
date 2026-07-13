# Carpeta files/

Esta carpeta contiene archivos estáticos que los roles copian a los servidores.

## Contenido

| Archivo | Usado por | Destino en servidor |
|---------|-----------|---------------------|
| `index.html` | rol frontend | `/var/www/html/index.html` |
| `init.sql` | rol database | `/tmp/init.sql` (ejecutado por psql) |
| `app.jar` | rol backend | `/opt/app/app.jar` |

## Nota sobre app.jar

El archivo `app.jar` NO se incluye en git (es binario pesado).
Para generarlo, compila el proyecto Spring Boot:

```bash
cd /ruta/a/spring-backend
mvn clean package -DskipTests
cp target/demo-0.0.1-SNAPSHOT.jar /ruta/a/ansible-fullstack-lab/files/app.jar
```

O usa un placeholder vacío para probar el flujo de Ansible:

```bash
touch files/app.jar
```
