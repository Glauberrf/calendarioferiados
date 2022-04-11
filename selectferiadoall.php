<?php
include ('connection.php');

$tabela = $_GET['tabela'];

//'".$tabela."'
$sql = "select data_registro, data_feriado, tipo, cidade, motivo from feriados_tb";

$result =  mysqli_query($connect, $sql);

$row = array();
if(mysqli_num_rows($result)>0){
	while ($rows = mysqli_fetch_assoc($result)) {
		$var = ['data_registro' => $rows['data_registro'],'data_feriado' => $rows['data_feriado'],'tipo' => $rows['tipo'],'cidade' => $rows['cidade'],'motivo' => $rows['motivo']];
		array_push($row, $var);
		//header('Content-Type: application/json');
	}
	echo json_encode($row);
}


?>