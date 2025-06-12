CREATE DATABASE contacto_db;
Use contacto_db;
CREATE TABLE formulario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    telefono VARCHAR(20),
    fecha DATE,
    asunto VARCHAR(255),
    mensaje TEXT
);

DROP TABLE formulario;

SELECT * FROM formulario;

INSERT INTO formulario (nombre, correo, telefono, fecha, asunto, mensaje)
VALUES ('Luis Torres', 'luis@example.com', '987654321', '2025-06-12', 'Consulta general', 'Estoy interesado en su producto');
-- 5. Actualizar datos (U - UPDATE)
UPDATE formulario
SET nombre = 'Luis Alberto Torres', asunto = 'Consulta técnica'
WHERE id = 1;
