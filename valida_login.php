<?php
	//Inicia a seção 
	session_start();
	// Recebe os dados dos campos usuário e senha
	$usuariot = $_POST['usuario'];
	$senhat = $_POST['senha'];
	// Printar na tela o que foi digitado nos campos, apenas para testar!
	//echo $usuariot.'-'.$senhat;
	//Conectando com o banco de dados
	include_once("conexao.php");
	//Codificação para consulta no banco de dados. 
	$sqlcod=("SELECT * FROM usuarios WHERE login='".$usuariot."' AND senha='".$senhat."' LIMIT 1");
	//Verificando se o os dados de login e senha consta na banco de dados
	$resultadosql=mysqli_query($conectar,$sqlcod);
	if(mysqli_num_rows($resultadosql)>=1){
    	$resultado = mysqli_fetch_array($resultadosql);
    	//Variável global para que outra pagina (administrativo.php) acesse a informação passada.
    	$_SESSION['usuarioId'] = $resultado['id'];
    	$_SESSION['usuarioNome'] = $resultado['nome'];
    	$_SESSION['usuarioNivelAcesso'] = $resultado['nivel_acesso_id'];
    	$_SESSION['usuarioLogin'] = $resultado['login'];
    	$_SESSION['usuarioEmail'] = $resultado['email'];
    	header("Location: administrativo.php");
  		//echo "Usuario: ".$resultado['nome'];

 
	}else{
		echo "utilizador nao encontrado ou erro";
		$_SESSION['loginErro'] = "Usuário ou senha inválido";
		header("Location: login.php");
    }
?>
