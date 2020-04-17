<?php
        $bomba = "Desligado";
        if($_REQUEST["numero"] != ""){
            switch($_REQUEST["numero"]){
                case "Ligar Bomba": shell_exec("sudo python ligarele.py"); $bomba = "Acionado"; break;
                case "Desligar Bomba": shell_exec("sudo python lowrele.py"); $bomba = "Desligado"; break;
            }
        }
	include_once("conexao.php");
	$consulta = "SELECT * FROM sensores ORDER BY id DESC";
	$resultadosql=mysqli_query($conectar,$consulta);
	$dado = mysqli_fetch_array($resultadosql);
	//echo $dado["id"];
	//echo $dado["nome"];
	//echo $dado["email"];
        shell_exec("sudo python Sensores/dados/sensores.py")
        
?>

<h1 class="page-header">Tempo Real</h1>

          <div class="row placeholders">
		  <div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/acionamento.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>Irrigação</h4>
              <span class="text-muted"><?php echo $bomba; ?></span>
            </div>
            <div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/solo.png" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
              <h4>Umidade do Solo</h4>
              <span class="text-muted"><?php echo $dado["humidadesolo"]; ?> %</span>
            </div>
            <div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/temp.png" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
              <h4>Temperatura</h4>
              <span class="text-muted"><?php echo $dado["temperatura"]; ?> ºC</span>
            </div>
            <div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/luz.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
              <h4>Luminosidade</h4>
              <span class="text-muted"><?php echo $dado["luminosidade"]; ?> %</span>
            </div>
            <div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/chuva1.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>Chuva</h4>
              <span class="text-muted"><?php echo $dado["chuva"]; ?></span>
            </div>
			<div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/umidadear.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>Umidade</h4>
              <span class="text-muted"><?php echo $dado["humidade"]; ?> %</span>
            </div>
			<div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/pressao.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>Pressão Atmosferica</h4>
              <span class="text-muted"><?php echo $dado["pressao"]; ?> hPa</span>
            </div>
			<div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/altitude.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>Altitude</h4>
              <span class="text-muted"><?php echo $dado["altitude"]; ?> m</span>
            </div>
			<div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/nivel.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>Nivel</h4>
              <span class="text-muted"><?php echo $dado["nivel"]; ?></span>
            </div>
			<div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/fluxo.png" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>Fluxo</h4>
              <span class="text-muted"><?php echo $dado["fluxo"]; ?></span>
            </div>
			<div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/tempagua.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>Temperatura da Água</h4>
              <span class="text-muted"><?php echo $dado["temp"]; ?> ºC</span>
            </div>
			<div class="col-xs-6 col-sm-3 placeholder">
              <img src="img/ph.png" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail"">
              <h4>pH</h4>
              <span class="text-muted"><?php echo $dado["id"]; ?></span> 
            </div>
          </div>
          
          
           
           <form action="administrativo.php" method="get">
             <input type="submit" name="numero" id="ligar" value="Ligar Bomba">
             <input type="submit" name="numero" id="desligar" value="Desligar Bomba">
            </form>
    
          
        </div>
      </div>