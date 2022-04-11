<?php
include ('connection.php');

$sql = "select userId, jogo, numeros from jogos";

$result =  mysqli_query($connect, $sql);

if(mysqli_num_rows($result)>0){
	while ($row = mysqli_fetch_assoc($result)) {
		echo json_encode("|userId".$row['userId']."|jogo".$row['jogo']."|numeros".$row['numeros'].";");



	}
}


?>