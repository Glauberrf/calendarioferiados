<?php
include ('connection.php');

$tabela = $_GET['tabela'];
$dataReg = $_GET['data_registro'];
$dataFer = $_GET['data_feriado'];
$tipo = $_GET['tipo'];
$cidade = $_GET['cidade'];
$motivo = $_GET['motivo'];






$sql = "insert into ".$tabela." (data_registro, data_feriado, tipo, cidade, motivo) values ('".$dataReg."','".$dataFer."','".$tipo."','".$cidade."','".$motivo."')";
$result =  mysqli_query($connect, $sql);

?>