CREATE DATABASE sistema;

\c sistema

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE enderecos (
    id SERIAL PRIMARY KEY,
    usuario_id SERIAL REFERENCES usuarios(id),
    rua VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    cep VARCHAR(20) NOT NULL
);  