<?php
$user_name = $_POST['user_name'];
$upassword = $_POST['upassword'];
	
	if($_POST['user_name'] && $_POST['upassword']){
		
		$servername = 'localhost';
		$username = 'root';
		$password = '';

		// Create connection
		$con = new mysqli($servername, $username, $password, "pw5");

		// Check connection
		if ($con->connect_error) {
			die("Connection failed: " . $con->connect_error);
		} 
		
		//selecting user from database
		$query = "SELECT * FROM users WHERE username='".$user_name."'";
		$results = mysqli_query($con,$query);
		if($results->num_rows >0){
			//Password verification
			$result  = mysqli_fetch_assoc($results);
			if(password_verify($upassword,$result['password'])){
				session_start();
				$_SESSION["user_name"] = $_POST['user_name'];	
				header("Location: welcome.php");
			}
			else{
				//if wrong password
				header("Location: login.html");
			}
		}	
		else{
			//if no user found
			header("Location: login.html");
		}		
	}
	else{
		// if input is missing
		header("Location: login.html");
	}
?>