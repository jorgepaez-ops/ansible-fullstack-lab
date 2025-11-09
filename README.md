# 📝 Resumen del laboratorio Fullstack con Docker y Ansible

## 1️⃣ Objetivo

Montar un **entorno fullstack de prueba** con tres nodos:

1. **Frontend**: Nginx simple con HTML/JS.
2. **Backend**: Spring Boot (Java) que expone un API REST.
3. **Base de datos**: PostgreSQL con una tabla consumida por el backend y el frontend.

Todo de manera reproducible con **Docker Compose** y automatizable con **Ansible**.

---

## 2️⃣ Estructura de proyectos

### 2.1 Código Java (spring-backend)

```
spring-backend/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/com/example/
│   │   └── resources/application.properties
│   └── test/
└── target/
    └── demo-0.0.1-SNAPSHOT.jar
```

* Contiene la app Spring Boot.
* Se compila desde el Dockerfile o IntelliJ/Maven.
* `application.properties` usa **variables de entorno** para conectar a PostgreSQL:

```properties
spring.datasource.url=${SPRING_DATASOURCE_URL}
spring.datasource.username=${SPRING_DATASOURCE_USERNAME}
spring.datasource.password=${SPRING_DATASOURCE_PASSWORD}
spring.jpa.hibernate.ddl-auto=${SPRING_JPA_HIBERNATE_DDL_AUTO:update}
```
---

### 2.2 Proyecto Ansible (ansible-fullstack-lab)

```
ansible-fullstack-lab/
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.ubuntu
├── roles/
│   ├── backend/tasks/main.yml
│   ├── database/tasks/main.yml
│   └── frontend/tasks/main.yml
└── inventory.ini
```

* `Dockerfile.backend` → Multi-stage build para compilar y ejecutar Spring Boot.
* `Dockerfile.ubuntu` → Opcional, para nodos tipo VM con SSH y utilidades de administración.
* Roles Ansible → Orquestación de contenedores o despliegue tradicional (systemd).

---

## 3️⃣ Dockerfile.backend (multi-stage)

```dockerfile
# Etapa build
FROM maven:3.9.9-eclipse-temurin-21 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -B
COPY src ./src
RUN mvn clean package -DskipTests

# Etapa runtime
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

✅ Permite compilar el `.jar` dentro del contenedor y ejecutarlo sin instalar Java en el host.

---

## 4️⃣ docker-compose.yml (ejemplo)

```yaml
version: "3.9"

services:
  database:
    image: postgres:16
    container_name: node1
    environment:
      POSTGRES_USER: demo
      POSTGRES_PASSWORD: demo
      POSTGRES_DB: messagesdb
    ports:
      - "5432:5432"
    networks:
      - fullstack-net

  backend:
    build:
      context: /home/jorge/IdeaProjects/spring-backend
      dockerfile: ./ansible-fullstack-lab/Dockerfile.backend
    container_name: node2
    depends_on:
      - database
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://database:5432/messagesdb
      SPRING_DATASOURCE_USERNAME: demo
      SPRING_DATASOURCE_PASSWORD: demo
    ports:
      - "8080:8080"
    networks:
      - fullstack-net

  frontend:
    image: nginx:latest
    container_name: node3
    depends_on:
      - backend
    volumes:
      - ./roles/frontend/html:/usr/share/nginx/html
    ports:
      - "80:80"
    networks:
      - fullstack-net

networks:
  fullstack-net:
    driver: bridge
```

---

## 5️⃣ Conceptos clave aprendidos

1. **Docker vs VM tradicional**

   * Contenedor: proceso aislado, no servidor completo.
   * Multi-stage build permite separar **compilación** de **runtime**.
   * No necesitas instalar Java en el host para correr tu backend.

2. **Administración de contenedores**

   * `docker logs` → ver logs de la app.
   * `docker exec -it <container> bash` → acceso interactivo.
   * `restart: always` → reinicio automático de contenedor si falla.

3. **Integración con Ansible**

   * Roles pueden levantar stack completo (`docker-compose`) o desplegar `.jar` en VMs.
   * Mantener Dockerfile separado del código fuente permite pipelines tipo Jenkins/GitLab CI.

4. **Preparación para AWS**

   * Backend compilado en contenedor → fácilmente trasladable a **ECS o EKS**.
   * Variables de entorno → equivalentes a parámetros en **ECS task** o **Lambda environment variables**.
   * Logs y debugging → equivalentes a **CloudWatch logs** o `kubectl logs`.

---

## 6️⃣ Flujo de trabajo recomendado

1. Levantar la base de datos y backend desde código:

```bash
docker-compose up -d --build
```

2. Verificar logs:

```bash
docker logs -f node2
```

3. Entrar al contenedor si es necesario:

```bash
docker exec -it node2 bash
```

4. Actualizar backend (código nuevo):

```bash
docker-compose build backend
docker-compose up -d backend
```

5. Frontend con Nginx → modificar archivos HTML directamente en volumen:

```bash
./roles/frontend/html/index.html
```

---

## 7️⃣ Notas finales

* Docker es **para despliegues reproducibles**, no reemplaza la administración tradicional de servidores.
* Puedes combinar imágenes ligeras para producción y contenedores tipo “nodo completo” si quieres **acceso SSH y herramientas**.
* Este laboratorio te prepara directamente para **CI/CD y despliegues en AWS** usando contenedores y pipelines modernos.

