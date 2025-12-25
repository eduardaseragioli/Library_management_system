use biblioteca_query;
-- ---------------------------------------------------------------------------------------
-- CONSULTAS BÁSICAS COM SELECT, FROM, ORDER BY, LIMIT, DISTINCT

-- 1. Selecionar todos os nomes dos leitores ordenados alfabeticamente
SELECT nome FROM Leitor
ORDER BY nome;

-- 2. Mostrar os 3 primeiros títulos de itens disponíveis
SELECT titulo FROM Item
WHERE disponivel = 1
LIMIT 3;

-- 3. Mostrar os diferentes idiomas dos itens
SELECT DISTINCT idioma FROM Item;

-- CONSULTAS COM OPERADORES, FUNÇÕES MATEMÁTICAS, DE TEXTO E DATA

-- 4. Obter o título do item com ISBN a 9789726081890
SELECT titulo, ISBN FROM Item
WHERE ISBN = 9789726081890;

-- 5. Mostrar o nome em maiúsculas dos leitores
SELECT UPPER(nome) AS "nome_maiusculas" FROM Leitor;

-- 6. Calcular a data prevista de devolução (data_emprestimo + duracao_dias)
SELECT idEmprestimo, DATE_ADD(data_emprestimo, INTERVAL duracao_dias DAY) AS data_devolucao_prevista
FROM Emprestimo;

-- CONSULTAS COM FUNÇÕES DE AGREGAÇÃO

-- 7. Número total de empréstimos
SELECT COUNT(*) AS "total_emprestimos" FROM Emprestimo;

-- 8. Valor médio das multas aplicadas
SELECT AVG(valor) AS "media_multas" FROM Multa;

-- CONSULTAS COM WHERE E OPERADORES LÓGICOS

-- 9. Leitores com nome começando por 'C' ou 'M'
SELECT * FROM Leitor
WHERE nome LIKE 'C%' OR nome LIKE 'M%';

-- 10. Itens com género Romance e tipo Livro
SELECT titulo FROM Item
WHERE genero = 'Romance' AND tipo_item = 'Livro';

-- 11. Multas com valor maior que 1 e não pagas
SELECT * FROM Multa
WHERE valor > 1 AND pago = 0;

-- 12. Empréstimos com duração entre 5 e 15 dias
SELECT * FROM Emprestimo
WHERE duracao_dias BETWEEN 5 AND 15;

-- CONSULTAS COM LIKE

-- 13. Leitores com email do Gmail
SELECT nome, email FROM Leitor
WHERE email LIKE '%@gmail.com';

-- 14. Funcionários cujo nome contém 'a'
SELECT nome FROM Funcionario
WHERE nome LIKE '%a%';

-- CONSULTAS COM GROUP BY E HAVING

-- 15. Contar número de itens por autor
SELECT idAutor, COUNT(*) AS total_itens
FROM Item
GROUP BY idAutor;

-- 16. Contar empréstimos por leitor
SELECT idLeitor, COUNT(*) AS total_emprestimos
FROM Emprestimo
GROUP BY idLeitor;

-- 17. Multas agrupadas por valor
SELECT valor, COUNT(*) AS quantidade
FROM Multa
GROUP BY valor;

-- 18. Leitores com mais de um empréstimo
SELECT idLeitor, COUNT(*) AS total
FROM Emprestimo
GROUP BY idLeitor
HAVING total > 1;

-- CONSULTAS COM INNER JOIN

-- 19. Obter nome do leitor e título do item emprestado
SELECT L.nome AS leitor, I.titulo
FROM Emprestimo E
INNER JOIN Leitor L ON E.idLeitor = L.idLeitor
INNER JOIN Item I ON E.idItem = I.idItem;

-- 20. Títulos e autores dos itens
SELECT I.titulo, A.nome AS autor
FROM Item I
INNER JOIN Autor A ON I.idAutor = A.idAutor;

-- 21. Nome do funcionário e itens que emprestou
SELECT F.nome AS funcionario, I.titulo
FROM Emprestimo E
INNER JOIN Funcionario F ON E.idFuncionario = F.idFuncionario
INNER JOIN Item I ON E.idItem = I.idItem;

-- 22. Leitor, título do item e valor da multa (se existir)
SELECT L.nome, I.titulo, M.valor
FROM Emprestimo E
INNER JOIN Leitor L ON E.idLeitor = L.idLeitor
INNER JOIN Item I ON E.idItem = I.idItem
INNER JOIN Multa M ON E.idEmprestimo = M.idEmprestimo;

-- 23. Leitores com multas por atraso
SELECT DISTINCT L.nome, M.valor
FROM Multa M
INNER JOIN Emprestimo E ON M.idEmprestimo = E.idEmprestimo
INNER JOIN Leitor L ON E.idLeitor = L.idLeitor
WHERE M.valor > 0;

-- CONSULTAS COM LEFT/RIGHT JOIN

-- 24. Mostrar todos os empréstimos, mesmo os que não têm multa
SELECT E.idEmprestimo, M.valor
FROM Emprestimo E
LEFT JOIN Multa M ON E.idEmprestimo = M.idEmprestimo;

-- 25. Mostrar todas as multas e os nomes dos leitores (pode haver multas sem leitor associado corretamente)
SELECT M.idMulta, L.nome
FROM Multa M
RIGHT JOIN Emprestimo E ON M.idEmprestimo = E.idEmprestimo
RIGHT JOIN Leitor L ON E.idLeitor = L.idLeitor;

-- CONSULTAS COM VIEW

-- 26. Criar uma VIEW de empréstimos detalhados
CREATE VIEW vw_emprestimos_detalhados AS
SELECT E.idEmprestimo, L.nome AS leitor, I.titulo AS item, E.data_emprestimo, E.duracao_dias, F.nome AS funcionario
FROM Emprestimo E
JOIN Leitor L ON E.idLeitor = L.idLeitor
JOIN Item I ON E.idItem = I.idItem
JOIN Funcionario F ON E.idFuncionario = F.idFuncionario;

-- 27. Usar a VIEW criada para listar os empréstimos de duração superior a 10 dias
SELECT * FROM vw_emprestimos_detalhados
WHERE duracao_dias > 10;


