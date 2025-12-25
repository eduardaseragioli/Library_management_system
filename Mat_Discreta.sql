use biblioteca_query;

--   média de empréstimos por leitor-- 
SELECT AVG(emp_por_leitor) AS 'Média de empréstimos por leitor'
FROM (
    SELECT COUNT(*) AS emp_por_leitor
    FROM Emprestimo
    GROUP BY idLeitor
) AS sub;

 -- ---Desvio padrao das multas aplicadas--- 
  SELECT MAX(valor) AS 'Valor Máximo da Multa', MIN(valor) AS 'Valor Mínimo da Multa'
FROM Multa;   

--  ---- O titulo do livro mais requistitado(moda) ---
SELECT i.titulo, COUNT(*) AS 'Nº de Empréstimos'
FROM Emprestimo e
JOIN Item i ON e.idItem = i.idItem
GROUP BY i.titulo
ORDER BY 2 DESC
LIMIT 1;

-- contagem dos empréstimos que resultaram em multas não pagas--
SELECT m.idMulta, e.idLeitor, l.nome, m.valor
FROM Multa m
JOIN Emprestimo e ON m.idEmprestimo = e.idEmprestimo
JOIN Leitor l ON e.idLeitor = l.idLeitor
WHERE m.pago = 0;

-- -- média de empréstimos por funcionário-- 
SELECT COUNT(*) / COUNT(DISTINCT idFuncionario) AS 'Média de empréstimos por funcionário'
FROM Emprestimo;



