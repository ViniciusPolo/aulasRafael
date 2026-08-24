const API = "http://localhost:8000/backend/api/usuarios.php";

const nome = document.querySelector("#nome");
const email = document.querySelector("#email");
const lista = document.querySelector("#lista");
const botao = document.querySelector("#btnSalvar");
const botaoDeletar = document.querySelector("#btnDeletar");

listarUsuarios();

botao.addEventListener("click", cadastrarUsuario);

async function listarUsuarios(){

    const resposta = await fetch(API);

    const usuarios = await resposta.json();

    lista.innerHTML = "";

    usuarios.forEach(usuario => {

        lista.innerHTML += `

            <div class="usuario">

                <strong>${usuario.nome}</strong>

                <br>

                ${usuario.email}

                <br>

                <button id="btnDeletar" onclick="deletarUsuario(${usuario.id})">
                    Deletar
                </button>

            </div>

        `;

    });

}

async function cadastrarUsuario(){

    const usuario = {

        nome: nome.value,

        email: email.value

    };

    const resposta = await fetch(API,{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify(usuario)

    });

    const resultado = await resposta.json();
    console.log(resultado);
    alert("Cadastrado com sucesso!");

    nome.value="";

    email.value="";

    listarUsuarios();

}

async function deletarUsuario(id){

    const resposta = await fetch(`${API}?id=${id}`,{

        method:"DELETE"

    });

    alert("Deletado com sucesso!");

    listarUsuarios();

}