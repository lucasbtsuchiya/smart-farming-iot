<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd >
<html xmlns="http://www.w3.org/1999/xhtml">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<?php header("Content-Type: text/html;  charset=ISO-8859-1",true); ?>
<html>
<head>
	<title>Cadastro</title>
    
    <!-- Bootstrap -->
    
</head>
<body> 	

	<div id="Layer1" style="position: absolute; left: 20px; top: 10px; width: 485px; height: 161px; z-index: 1; margin-left: 5px">
		<h1 align="justify">Cadastro</h1>
		<form id="form1" name="signup" method="post" action="cadastrando.php">
			<p>
				<label for="nome">Nome Completo</label>
				<input type="text" name="nome" id="nome" />
				<label for="profissao">Profissão</label>
				<input type="text" name="profissao" id="profissao" />
				<label for="instituicao">Instituição</label>
				<input type="text" name="instituicao" id="instituicao" />
				<label for="cidade">Cidade - Estado</label>
				<input type="text" name="cidade" id="cidade" />
				<label for="email">E-mail</label>
				<input type="text" name="email" id="email" />
				<label for="login">Login</label>
				<input type="text" name="login" id="login" />
				<label for="senha">Senha</label>
				<input type="password" name="senha" id="senha" />
				<label for="senha">Seu Armazenamento</label>
				<div class="radio">
					
					<label>
						<input type="radio" name="optionsRadios" id="optionsRadios1" value="option1" checked>
						Google Drive
					</label>
				</div>
				<div class="radio">
					<label>
						<input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">
						Dropbox
					</label>
				</div>
				
				<input type="submit" value="cadastrar" />
				
			</p>
		</form>
		<p align="justify">&nbsp;</p>
	</div>
	<div align="center">
		<script src="js/bootstrap.min.js"></script>
	</div>
  
</body>
</html>
