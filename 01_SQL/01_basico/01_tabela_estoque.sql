CREATE TABLE estoque (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price NUMERIC,
    tipo TEXT,
    color TEXT,
    fabrication INTEGER
);

INSERT INTO estoque VALUES 
    (1, 'Fusca', 14000, 'carro', 'branco', 1975),
    (2, 'Uno', 22000, 'carro', 'vermelho', 2011),
    (3, 'Intruder', 8000, 'moto', 'verde', 2008),
    (4, 'Factor', 10000, 'moto', 'preto', 2010),
    (5, 'Palio', 30000, 'carro', 'branco', 2014),
    (6, 'Civic', 55000, 'carro', 'prata', 2018),
    (7, 'Corolla', 60000, 'carro', 'preto', 2019),
    (8, 'Hornet', 25000, 'moto', 'vermelho', 2015),
    (9, 'Bros', 12000, 'moto', 'vermelho', 2017),
    (10, 'Titan', 9000, 'moto', 'azul', 2012),
    (11, 'Gol', 18000, 'carro', 'branco', 2013),
    (12, 'Onix', 32000, 'carro', 'prata', 2016),
    (13, 'Fazer', 15000, 'moto', 'azul', 2014),
    (14, 'XRE', 18000, 'moto', 'branco', 2018),
    (15, 'Saveiro', 25000, 'carro', 'prata', 2015);