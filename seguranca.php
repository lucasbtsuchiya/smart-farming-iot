<?php
	
	ob_start();
	if (($_SESSION['usuarioId'] == "") || ($_SESSION['usuarioNome'] == "") || ($_SESSION['usuarioNivelAcesso'] == "") || ($_SESSION['usuarioLogin'] == "")){
		 unset(
        $_SESSION['usuarioId'],
        $_SESSION['usuarioNome'],
        $_SESSION['usuarioNivelAcesso'],
        $_SESSION['usuarioLogin'],
        $_SESSION['usuarioEmail']
      );

		//Mensagem de erro.
		$_SESSION['loginErro'] = "Área restrita para usuários cadastrados";
		//Redireciona o usuário para a tela de login
		header("Location: login.php");
	}
?>