CREATE DATABASE "restaurante_laLlama"
 USE "restaurante_laLLama"

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dia VARCHAR(15) NOT NULL,
    menu_completo TEXT NOT NULL
);

-- Metes todo de una sola vez
INSERT INTO menus_semanales (dia, menu_completo) VALUES 
('Lunes', 'Ajiaco santafereño, arroz, aguacate y pollo desmenuzado.'),
('Martes', 'Bandeja paisa tradicional con frijoles, carne molida y chicharrón.'),
('Miércoles', 'Sancocho de gallina con yuca, plátano y mazorca.'),
('Jueves', 'Sobrebarriga en salsa criolla con papa cocida y arroz.'),
('Viernes', 'Pescado frito con patacón, arroz de coco y ensalada.'),
('Sábado', 'Fritanga colombiana con rellena, chorizo y papa criolla.'),
('Domingo', 'Mondongo o sancocho de costilla.');
