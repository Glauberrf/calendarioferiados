<?php
include ('connection.php');

$sql = "select userId, jogo, numeros from jogos";

$result =  mysqli_query($connect, $sql);

$row = array();
if(mysqli_num_rows($result)>0){
	while ($rows = mysqli_fetch_assoc($result)) {
		$var = ['UserId' => $rows['userId'],'Logo' => $rows['jogo'],'Numeros' => $rows['numeros']];
		array_push($row, $var);
		//header('Content-Type: application/json');
	}
	echo json_encode($row);
}


?>