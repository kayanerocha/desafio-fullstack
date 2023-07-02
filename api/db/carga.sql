INSERT desafio_cotacao.tb_parceiros (nome, cnpj, endereco, uf_cobertura)
VALUES ('01TELECOM', '11111111111111', 'R. Santa Cruz, 131 - Paulicéia, São Bernardo do Campo - SP, 09683-050', 'SP'),
('02TELECOM', '22222222222222', 'R. Bernardo Guimarães, 108 - Taboão, Diadema - SP, 09940-320', 'RJ'),
('03TELECOM', '33333333333333', 'R. João Batista de Almeida, 150 - Vila Florida, São Bernardo do Campo - SP, 09661-010', 'SP;RJ'),
('04TELECOM', '44444444444444', 'R. Jequitibá, 50 - Vale do Sereno, Nova Lima - MG, 34006-033', 'MG'),
('05TELECOM', '55555555555555', 'Av. Barbacena, 235 - Santo Agostinho, Belo Horizonte - MG, 30190-130, 34006-033', 'MG;SP'),
('06TELECOM', '66666666666666', 'R. Arceburgo, 200 - Bonfim, Belo Horizonte - MG, 31210-370', 'MG;SP;RJ'),
('07TELECOM', '77777777777777', 'R. Visc. de Parnaíba, 1568 - Brás, São Paulo - SP, 03164-300', 'SP;RJ;MG'),
('08TELECOM', '88888888888888', 'R. Pedro Alves, 307 - Santo Cristo, Rio de Janeiro - RJ, 20220-284', 'MG;SP;RJ'),
('09TELECOM', '99999999999999', 'R. do Monte, 27 - Gamboa, Rio de Janeiro - RJ, 20221-130', 'RJ'),
('10TELECOM', '10101010101010', 'Av. da Liberdade - Liberdade, São Paulo - SP, 01503-000', 'MG;SP');


INSERT INTO desafio_cotacao.tb_viabilidades (logradouro, numero, bairro, cidade, uf, produto, velocidade)
VALUES ('R. Padre Manuel Godinho', '382', 'Vila Clara', 'São Paulo', 'SP', 'VPN VIP', '20 MBPS'),
('R. Pref. Olímpio de Melo', '1105', 'Benfica', 'Rio de Janeiro', 'RJ', 'IP Connect', '50 MBPS'),
('R. Pref. Olímpio de Melo', '1105', 'Benfica', 'Rio de Janeiro', 'RJ', 'IP Connect', '50 MBPS'),
('R. José Fernandes', '20', 'Jardim Vilas Boas', 'São Paulo', 'SP', 'VPN VIP', '30 MBPS'),
('Av. Pres. Antônio Carlos', '251', 'Centro', 'Rio de Janeiro', 'RJ', 'IP Connect', '5 MBPS'),
('Avenida Graça Aranha', '326', 'Centro', 'Rio de Janeiro', 'RJ', 'IP Connect', '10 MBPS'),
('R. Cuiabá', '55', 'Prado', 'Belo Horizonte', 'MG', 'IP Connect', '15 MBPS'),
('R. São Paulo', '2249', 'Lourdes', 'Belo Horizonte', 'MG', 'IP Connect', '25 MBPS'),
('R. Sergipe', '461', 'Boa Viagem', 'Belo Horizonte', 'MG', 'IP Connect', '60 MBPS'),
('Rua dos Carijos', '108', '', 'Belo Horizonte', 'MG', 'IP Connect', '50 MBPS');


INSERT INTO desafio_cotacao.tb_resultados_viabilidades (resultado, id_viabilidade, id_parceiro)
VALUES ('Viável', 2, 1),
('Inviável', 2, 3),
('Projeto Especial', 2, 10),
('Viável', 3, 2),
('Projeto Especial', 3, 3);
