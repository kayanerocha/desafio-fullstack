INSERT tb_parceiros (nome, cnpj, endereco, uf_cobertura)
VALUES ('01TELECOM', '11111111111111', 'R. Santa Cruz, 131 - Paulicéia, São Bernardo do Campo - SP, 09683-050', 'SP'),
('02TELECOM', '22222222222222', 'R. Bernardo Guimarães, 108 - Taboão, Diadema - SP, 09940-320', 'RJ'),
('03TELECOM', '33333333333333', 'R. João Batista de Almeida, 150 - Vila Florida, São Bernardo do Campo - SP, 09661-010', 'SP;RJ');

INSERT tb_parceiros (nome, cnpj, endereco, uf_cobertura)
VALUES ('04TELECOM', '44444444444444', 'R. Jequitibá, 50 - Vale do Sereno, Nova Lima - MG, 34006-033', 'MG');

INSERT INTO tb_viabilidades (logradouro, numero, bairro, cidade, uf, produto, velocidade)
VALUES ('Rua Wilson Kawanami', '77', 'Jardim Lourdes', 'São Paulo', 'SP', 'IP Connect', '10 MBPS'),
('R. Padre Manuel Godinho', '382', 'Vila Clara', 'São Paulo', 'SP', 'VPN VIP', '20 MBPS'),
('R. Pref. Olímpio de Melo', '1105', 'Benfica', 'Rio de Janeiro', 'RJ', 'IP Connect', '50 MBPS'),
('R. Pref. Olímpio de Melo', '1105', 'Benfica', 'Rio de Janeiro', 'RJ', 'IP Connect', '50 MBPS');

use desafio_cotacao;
select * from tb_viabilidades;
select uf from tb_viabilidades where id = 1;
select uf_cobertura from tb_parceiros where id = 3;
select * from tb_resultados_viabilidades;
select * from tb_parceiros;
select id from tb_resultados_viabilidades where id_viabilidade = 1 and id_parceiro = 4;
delete from tb_resultados_viabilidades where id = 2;

SELECT jsonb_agg(resultados) from (SELECT a.id, concat(b.logradouro, ', ', b.numero, ' - ', b.bairro, ', ', b.cidade, ' - ', b.uf) AS endereco,
a.resultado, c.nome AS nome_parceiro
FROM tb_resultados_viabilidades a
LEFT JOIN tb_viabilidades b ON b.id = a.id_viabilidade
LEFT JOIN tb_parceiros c ON c.id = a.id_parceiro) as resultados;