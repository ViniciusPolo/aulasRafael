<?php

// header("Content-Type: application/json");

// require_once "../config/database.php";
// require_once "../models/Usuario.php";

// $db = new Database();
// $conn = $db->conectar();

// $usuario = new Usuario($conn);

// $metodo = $_SERVER["REQUEST_METHOD"];
$metodo = "GET";

switch ($metodo) {

    case "GET":

        // echo json_encode(
        //     $usuario->listar()
        // );
        print_r("teste");

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

        $usuario->cadastrar(
            $dados["nome"],
            $dados["email"]
        );

        echo json_encode([
            "mensagem" => "Usuário cadastrado!"
        ]);

        break;

    default:

        http_response_code(405);

        echo json_encode([
            "erro" => "Método não permitido."
        ]);

}
