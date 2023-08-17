-- CONSTRUA UM PROJETO LÓGICO DE BANCO DE DADOS DO ZERO
-- CRIAÇÃO DO BANCO DE DADOS E TABELAS

-- Tabela Cliente: Armazena informações sobre os clientes.
CREATE TABLE Cliente (
    cliente_id INT PRIMARY KEY,
    nome VARCHAR(255),
    endereco VARCHAR(255),
    telefone VARCHAR(20)
);

-- Tabela Produto: Armazena informações sobre os produtos disponíveis.
CREATE TABLE Produto (
    produto_id INT PRIMARY KEY,
    nome VARCHAR(255),
    preco DECIMAL(10, 2)
);

-- Tabela Pedido: Armazena informações sobre os pedidos dos clientes.
CREATE TABLE Pedido (
    pedido_id INT PRIMARY KEY,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

-- Tabela ItemPedido: Armazena detalhes dos produtos em cada pedido.
CREATE TABLE ItemPedido (
    item_id INT PRIMARY KEY,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    FOREIGN KEY (pedido_id) REFERENCES Pedido(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
);

-- Tabela Fornecedor: Armazena informações sobre os fornecedores.
CREATE TABLE Fornecedor (
    fornecedor_id INT PRIMARY KEY,
    nome VARCHAR(255)
);

-- Tabela Estoque: Armazena informações sobre os produtos em estoque.
CREATE TABLE Estoque (
    estoque_id INT PRIMARY KEY,
    fornecedor_id INT,
    produto_id INT,
    quantidade INT,
    FOREIGN KEY (fornecedor_id) REFERENCES Fornecedor(fornecedor_id),
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
);

-- INSERÇÃO DE DADOS

-- Inserção de exemplos de cliente, produto, pedido e estoque.
INSERT INTO Cliente (cliente_id, nome, endereco, telefone)
VALUES (1, 'João', 'Rua A, 123', '123-4567');

INSERT INTO Produto (produto_id, nome, preco)
VALUES (1, 'Produto A', 60.00),
       (2, 'Produto B', 40.00),
       (3, 'Produto C', 70.00);

INSERT INTO Pedido (pedido_id, cliente_id)
VALUES (1, 1);

INSERT INTO ItemPedido (item_id, pedido_id, produto_id, quantidade)
VALUES (1, 1, 1, 2),
       (2, 1, 2, 3);

INSERT INTO Fornecedor (fornecedor_id, nome)
VALUES (1, 'Fornecedor X'),
       (2, 'Fornecedor Y');

INSERT INTO Estoque (estoque_id, fornecedor_id, produto_id, quantidade)
VALUES (1, 1, 1, 5),
       (2, 2, 2, 8);
