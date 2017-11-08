<?php
    $a = $_GET['t'];
	$conn = new mysqli('localhost','root','123456','translate');  
	if(!$conn){  
	    die("error:".mysqli_connect_error());  
	}  
	$sql = "SELECT chinese FROM trans WHERE english='{$a}'";
	$result=mysqli_query($conn,$sql); 
	$css = mysqli_fetch_array($result);
	echo json_encode($css[0]); 
	mysqli_close($conn); 
?>