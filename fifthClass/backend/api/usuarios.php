<?php

header("Content-Type: application/json");

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");
header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "OPTIONS") {
    http_response_code(200);
    exit;
}

require_once __DIR__ . "/../config/database.php";
require_once __DIR__ . "/../models/Usuario.php";

$db = new Database();
$conn = $db->conectar();

$usuario = new Usuario($conn);

$metodo = $_SERVER["REQUEST_METHOD"];

switch ($metodo) {

    case "GET":

        echo json_encode(
            $usuario->listar()
        );

        break;

    case "POST":
        $dados = json_decode(file_get_contents("php://input"), true);

        if (
            empty($dados["nome"]) ||
            empty($dados["email"])
        ) {

            http_response_code(400);

            echo json_encode([
                "erro" => "Dados inválidos."
            ]);

            exit;
        }

        $resultado = $usuario->cadastrar(
            $dados["nome"],
            $dados["email"]
        );


        echo json_encode([
            "resultado" => $resultado
        ]);

        exit;

    case "DELETE":
        $id = $_GET["id"] ?? null;

        if (!$id) {
            http_response_code(400);
            echo json_encode([
                "erro" => "ID não fornecido."
            ]);
            exit;
        }

        $usuario->deletar($id);

        echo json_encode([
            "mensagem" => "Usuário removido."
        ]);

        break;

    default:

        http_response_code(405);

        echo json_encode([
            "erro" => "Método não permitido."
        ]);

}
