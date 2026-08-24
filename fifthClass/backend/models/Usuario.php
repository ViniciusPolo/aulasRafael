<?php

class Usuario
{
    private PDO $conn;

    public function __construct(PDO $conn)
    {
        $this->conn = $conn;
    }

    public function listar()
    {
        $sql = "SELECT * FROM usuarios ORDER BY id";

        $stmt = $this->conn->prepare($sql);

        $stmt->execute();

        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function cadastrar($nome, $email)
    {
        $sql = "INSERT INTO usuarios (nome, email)
                VALUES (:nome, :email)";

        $stmt = $this->conn->prepare($sql);

        return $stmt->execute([
            ":nome" => $nome,
            ":email" => $email
        ]);
    }

    public function deletar($id)
    {
        $sql = "DELETE FROM usuarios WHERE id = :id";

        $stmt = $this->conn->prepare($sql);

        return $stmt->execute([
            ":id" => $id
        ]);
    }
}
