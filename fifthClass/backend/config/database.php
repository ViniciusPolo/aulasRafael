<?php

class Database
{
    private $host = "localhost";
    private $port = "5432";
    private $dbname = "sistema";
    private $user = "postgres";
    private $password = "senha";

    public function conectar()
    {
        try {

            $pdo = new PDO(
                "pgsql:host={$this->host};port={$this->port};dbname={$this->dbname}",
                $this->user,
                $this->password
            );

            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            return $pdo;

        } catch (PDOException $e) {

            die("Erro: " . $e->getMessage());

        }
    }
}
