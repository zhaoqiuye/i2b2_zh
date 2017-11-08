<?php
	$a = $_POST['t']; 
	$con = mysql_connect("192.168.214.128","root","");
	if (!$con){
	  	die('Could not connect: ' . mysql_error());
	}
	mysql_select_db("translate", $con);
	mysql_set_charset("utf8"); 
	$sql = "SELECT chinese FROM trans WHERE english='{$a}'";
	$res = mysql_query($sql,$con);
	$css=mysql_fetch_array($res);
	echo json_encode($css[0]);  
	mysql_close($con);
?>