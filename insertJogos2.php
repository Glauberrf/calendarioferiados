<?php
include ('connection.php');

$userId = $_GET['adduserId'];
$jogo = $_GET['addjogo'];
$numeros = $_GET['addnumero'];



$sql = "insert into jogos (userId, jogo, numeros) values ('".$userId."','".$jogo."','".$numeros."')";
$result =  mysqli_query($connect, $sql);

?>