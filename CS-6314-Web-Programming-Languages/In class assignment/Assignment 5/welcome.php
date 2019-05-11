<?php
	session_start();
	if(isset($_SESSION["user_name"])){
		
		$servername = 'localhost';
		$username = 'root';
		$password = '';

		// Create connection
		$con = new mysqli($servername, $username, $password, "pw5");

		// Check connection
		if ($con->connect_error) {
			die("Connection failed: " . $con->connect_error);
		} 
		
		$query = "SELECT * FROM users JOIN favoritebooks ON users.username=favoritebooks.username WHERE users.username='".$_SESSION["user_name"]."'";
		$results = mysqli_query($con,$query);
		
		$result  = mysqli_fetch_assoc($results);
		echo "<h3>Welcome : ". $result["fullname"]."</h3>";
		echo "<h3>Your favorite book is: ". $result["booktitle"]."</h3>";
		$avatar = $result["avatar"];
		
		?>
		
		<img src="<?php echo $avatar?>" alt="image">
	<?php	
	}
	else{
		session_unset();
		session_destroy();
		header("Location: login.html");
	}
?>