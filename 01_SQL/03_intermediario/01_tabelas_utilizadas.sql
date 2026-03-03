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

-- Tabela estoque (com data_entrada)
CREATE TABLE estoque (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    price DECIMAL(10,2),
    categoria_id INT,
    cor_id INT,
    fabrication INT,
    data_entrada DATE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id),
    FOREIGN KEY (cor_id) REFERENCES cores(id)
);

INSERT INTO estoque (id, nome, price, categoria_id, cor_id, fabrication, data_entrada) VALUES
(1, 'Fusca', 14000.00, 1, 1, 1975, '2025-01-15'),
(2, 'Uno', 22000.00, 1, 2, 2011, '2025-01-20'),
(3, 'Intruder', 8000.00, 2, 3, 2008, '2025-02-10'),
(4, 'Factor', 10000.00, 2, 4, 2010, '2025-02-15'),
(5, 'Palio', 30000.00, 1, 1, 2014, '2025-03-05'),
(6, 'Civic', 55000.00, 1, 5, 2018, '2025-03-12'),
(7, 'Corolla', 60000.00, 1, 4, 2019, '2025-04-01'),
(8, 'Hornet', 25000.00, 2, 2, 2015, '2025-04-08'),
(9, 'Bros', 12000.00, 2, 2, 2017, '2025-05-20'),
(10, 'Titan', 9000.00, 2, 6, 2012, '2025-05-25'),
(11, 'Gol', 18000.00, 1, 1, 2013, '2025-06-02'),
(12, 'Onix', 32000.00, 1, 5, 2016, '2025-06-10'),
(13, 'Fazer', 15000.00, 2, 6, 2014, '2025-07-01'),
(14, 'XRE', 18000.00, 2, 1, 2018, '2025-07-07'),
(15, 'Saveiro', 25000.00, 1, 5, 2015, '2025-08-14');

-- Tabela vendas
CREATE TABLE vendas (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT,
    data_venda DATE,
    preco_venda DECIMAL(10,2),
    cliente_nome VARCHAR(100),
    FOREIGN KEY (id_produto) REFERENCES estoque(id)
);

INSERT INTO vendas (id_produto, data_venda, preco_venda, cliente_nome) VALUES
(1, '2025-02-20', 13500.00, 'João Silva'),
(3, '2025-03-15', 7800.00, 'Maria Santos'),
(5, '2025-04-10', 29500.00, 'Carlos Oliveira'),
(8, '2025-05-05', 24000.00, 'Ana Souza'),
(11, '2025-06-30', 17500.00, 'Pedro Lima'),
(6, '2025-07-22', 54000.00, 'Paula Mendes');