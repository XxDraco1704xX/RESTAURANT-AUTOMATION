

CREATE DATABASE "restaurante_laLLama"
    DEFAULT CHARACTER SET = 'utf8mb4';
    
CREATE TABLE menus(
 id menu PRIMARY KEY INTEGER AUTO_INCREMENT,
 day VARCHAR(10) NOT NULL,
 day_menu TEXT NOT NULL,
);
CREATE TABLE clients(
    id PRIMARY KEY INTEGER  AUTO_INCREMENT
    names VARCHAR(100),
    whatsapp VARCHAR(13) UNIQUE,
);
CREATE TABLE orders(
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL FOREIGN KEY clients(id),
    menu_id INT NOT NULL FOREIGN KEY menus(id),
    fecha DATE NOT NULL,) ;  
    
