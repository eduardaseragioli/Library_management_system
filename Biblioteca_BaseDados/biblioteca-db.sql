Drop database if exists biblioteca_query;
create database if not exists biblioteca_query;
USE biblioteca_query;

CREATE TABLE Autor (
    idAutor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45) NOT NULL,
    nacionalidade VARCHAR(45) NOT NULL
);

CREATE TABLE Item (
    idItem INT AUTO_INCREMENT PRIMARY KEY,
    idAutor INT NOT NULL,
    editora VARCHAR(45) NOT NULL,
    genero ENUM('Romance', 'Comedia', 'Suspense', 'Biografia', 'Cientifico', 'Outro') NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    disponivel TINYINT(1) NOT NULL DEFAULT 1,
    ISBN DECIMAL(14,0) UNIQUE NOT NULL,
    tipo_item ENUM('Livro', 'Revista', 'Multimedia') NOT NULL,
    FOREIGN KEY (idAutor) REFERENCES Autor(idAutor)
);

CREATE TABLE Leitor (
    idLeitor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(45) NOT NULL UNIQUE,
    telemovel DECIMAL(9,0) NOT NULL,
    nif DECIMAL(9,0) UNIQUE NOT NULL
);

CREATE TABLE Funcionario (
    idFuncionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45) NOT NULL,
    telemovel DECIMAL(9,0) NOT NULL,
    nif DECIMAL(9,0) UNIQUE NOT NULL,
    email VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE Emprestimo (
    idEmprestimo INT AUTO_INCREMENT PRIMARY KEY,
    idFuncionario INT NOT NULL,
    idLeitor INT NOT NULL,
    idItem INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    duracao_dias INT NOT NULL CHECK (duracao_dias > 0),
    devolvido TINYINT(1) NOT NULL DEFAULT 0,
    FOREIGN KEY (idFuncionario) REFERENCES Funcionario(idFuncionario),
    FOREIGN KEY (idLeitor) REFERENCES Leitor(idLeitor),
    FOREIGN KEY (idItem) REFERENCES Item(idItem)
);

CREATE TABLE Multa (
    idMulta INT AUTO_INCREMENT PRIMARY KEY,
    idEmprestimo INT NOT NULL,
    valor DECIMAL(6,2) NOT NULL CHECK (valor >= 0),
    descricao VARCHAR(45),
    pago TINYINT(1) NOT NULL DEFAULT 0,
    FOREIGN KEY (idEmprestimo) REFERENCES Emprestimo(idEmprestimo)
);


-- -----------------------------------------------------
-- Table Autor
-- -----------------------------------------------------
INSERT INTO Autor (nome, nacionalidade)
VALUES 
('José Saramago', 'Português'),
('Isabel Allende', 'Chilena'),
('George Orwell', 'Britânico'),
('Neil deGrasse Tyson', 'Americano'),
('Margaret Atwood', 'Canadiana'),
('Haruki Murakami', 'Japonês'),
('Jane Austen', 'Britânica'),
('Stephen King', 'Americano'),
('Camilo Castelo Branco', 'Português'),
('Agustina Bessa-Luís', 'Portuguesa');
-- -----------------------------------------------------
-- Table Item
-- -----------------------------------------------------
INSERT INTO Item (idAutor, editora, genero, titulo, ISBN, tipo_item)
VALUES 
(1, 'Porto Editora', 'Romance', 'Ensaio sobre a Cegueira',978-972-0-04683-3, 'Livro'),
(2, 'Plaza & Janés', 'Romance', 'A Casa dos Espíritos', 978-972-0-04445-7, 'Livro'), 
(3, 'Penguin Books', 'Suspense', '1984', 9789726081890, 'Livro'), 
(4, '11 X 17', 'romance', 'Misery', 9789722527118, 'Livro'),
(5, 'CONTINUUM PUBLISHING CORPORATION', 'Romance', 'The Handmaid\'s Tale', 97817848748724, 'Livro'),
(6, 'Penguin Books', 'Outro', 'Animal Farm', 9780241341667, 'Livro'),
(7, 'Revista LER', 'Outro', 'LER - Edição 152', 97897284931891, 'Revista'),
(8, 'Planeta Comic', 'Outro', 'Veil', 9788411611244, 'Livro'),
(6, 'Shinchosha', 'Romance', 'Norwegian Wood', 9784101001548, 'Livro'),
(7, 'Penguin Classics', 'Romance', 'Pride and Prejudice', 9780141439518, 'Livro'),
(8, 'Scribner', 'Suspense', 'The Shining', 9780307743657, 'Livro'),
(9, 'Porto Editora', 'Romance', 'Amor de Perdição', 9789720012689, 'Livro'),
(10, 'Relógio D’Água', 'Romance', 'A Sibila', 9789896415819, 'Livro'),
(3, 'Revista Cultura', 'Outro', 'Revista Cultura Nº1', 9789720000001, 'Revista'),
(4, 'Discovery Channel', 'Cientifico', 'Cosmos: A Spacetime Odyssey', 9781234567891, 'Multimedia'),
(8, 'Revista Mistério', 'Suspense', 'Mistério Mensal Nº45', 9789720000002, 'Revista'),
(7, 'BBC', 'Biografia', 'Jane Austen: A Life', 9789876543210, 'Multimedia'),
(6, 'JBC', 'Outro', 'Kafka on the Shore', 9784101001586, 'Livro');
-- -----------------------------------------------------
-- Table Leitor
-- -----------------------------------------------------
INSERT INTO Leitor (nome, email, telemovel, nif)
VALUES 
('Carla Mota', 'carla.mota@gmail.com', 912345678, 123456789),
('Rui Costa', 'rui.costa@hotmail.com', 934567890, 987654321),
('Marta Sousa', 'marta.sousa@gmail.com', 911223344, 112233445),
('André Pinto', 'andre.pinto@hotmail.com', 919876543, 554433221),
('Bruno Oliveira', 'bruno.oliveira@gmail.com', 913456789, 101010101),
('Sílvia Mendes', 'silvia.mendes@outlook.com', 914567890, 202020202),
('Joana Martins', 'joana.martins@yahoo.com', 915678901, 303030303),
('Tiago Lopes', 'tiago.lopes@gmail.com', 916789012, 404040404),
('Inês Ferreira', 'ines.ferreira@hotmail.com', 917890123, 505050505),
('Carlos Almeida', 'carlos.almeida@sapo.pt', 918901234, 606060606);

-- -----------------------------------------------------
-- Table Funcionario
-- -----------------------------------------------------
INSERT INTO Funcionario (nome, telemovel, nif, email)
VALUES 
('Mariana Alves', 965432109, 123123123, 'mariana.alves@hotmail.com'),
('Tiago Ferreira', 967891234, 321321321, 'tiago.ferreira@Outlook'),
('Sofia Lima', 962345678, 456456456, 'sofia.lima@gmail.com'),
('José Mendes', 968112233, 111222333, 'jose.mendes@hotmail.com'),
('Ana Rocha', 969334455, 444555666, 'ana.rocha@gmail.com');

-- -----------------------------------------------------
-- Table Emprestimo
-- -----------------------------------------------------
INSERT INTO Emprestimo (idFuncionario, idLeitor, idItem, data_emprestimo, duracao_dias)
VALUES 
(1, 1, 1, '2025-03-01', 15),
(2, 2, 2, '2025-03-05', 10),
(1, 3, 4, '2025-05-10', 20),
(3, 4, 5, '2025-04-12', 7),
(2, 1, 6, '2025-04-15', 10),
(2, 2, 7, '2025-04-17', 5),
(3, 1, 8, '2025-04-18', 3),
(1, 5, 5, '2023-06-20', 14),
(2, 6, 10, '2025-04-21', 7),
(3, 7, 11, '2024-08-22', 10),
(4, 8, 12, '2023-04-23', 12),
(5, 9, 12, '2025-10-13', 8),
(4, 7, 14, '2025-04-25', 6),
(1, 2, 15, '2023-04-26', 10),
(2, 3, 16, '2025-04-27', 7),
(3, 4, 17, '2024-04-28', 5),
(4, 5, 18, '2025-04-29', 9),
(5, 6, 4, '2025-02-19', 15);

-- -----------------------------------------------------
-- Table Multa
-- -----------------------------------------------------
INSERT INTO Multa (idEmprestimo, valor, descricao, pago)
VALUES 
(1, 3.00, 'Atraso de 3 dias', 0),
(2, 0.00, 'Entregue a tempo', 1),
(3, 0.00, 'Entregue a tempo', 1),
(4, 5.00, 'Atraso de 5 dias', 0),
(5, 5.00, 'Atraso de 5 dias', 1),
(6, 0.00, 'Entregue a tempo', 1),
(7, 0.00, 'Entrega a tempo', 0),
(8, 4.00, 'Atraso de 4 dias', 0),
(9, 0.00, 'Entregue a tempo', 1),
(10, 14.00, 'Atraso de 14 dias', 1);


