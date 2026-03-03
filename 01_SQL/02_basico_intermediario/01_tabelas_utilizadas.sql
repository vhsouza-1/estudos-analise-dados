-- Tabela cores
CREATE TABLE cores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_cor VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO cores (nome_cor) VALUES 
('Branco'), ('Vermelho'), ('Verde'), ('Preto'), ('Prata'), ('Azul');

-- Tabela categorias
CREATE TABLE categorias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO categorias (nome_categoria) VALUES 
('Carro'), ('Moto');

-- Tabela estoque (com dados completos)
CREATE TABLE estoque (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    price DECIMAL(10,2),
    categoria_id INT,
    cor_id INT,
    fabrication INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id),
    FOREIGN KEY (cor_id) REFERENCES cores(id)
);

INSERT INTO estoque (id, nome, price, categoria_id, cor_id, fabrication) VALUES
(1, 'Fusca', 14000.00, 1, 1, 1975),
(2, 'Uno', 22000.00, 1, 2, 2011),
(3, 'Intruder', 8000.00, 2, 3, 2008),
(4, 'Factor', 10000.00, 2, 4, 2010),
(5, 'Palio', 30000.00, 1, 1, 2014),
(6, 'Civic', 55000.00, 1, 5, 2018),
(7, 'Corolla', 60000.00, 1, 4, 2019),
(8, 'Hornet', 25000.00, 2, 2, 2015),
(9, 'Bros', 12000.00, 2, 2, 2017),
(10, 'Titan', 9000.00, 2, 6, 2012),
(11, 'Gol', 18000.00, 1, 1, 2013),
(12, 'Onix', 32000.00, 1, 5, 2016),
(13, 'Fazer', 15000.00, 2, 6, 2014),
(14, 'XRE', 18000.00, 2, 1, 2018),
(15, 'Saveiro', 25000.00, 1, 5, 2015);