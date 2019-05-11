<html lang="en">
  <head>
    <title>Location</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script src="index.js"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style type="text/css">
      .container{
        padding: 50px;
        width: 40%;
        margin-top: 10%;
        border: 2px solid green;
        background-color: silver;
      }
    </style>
    <?php 
      $servername = "localhost";
      $username = "root";
      $password = "";
      $dbname = "countrylist";

      global $connection;
      $connection= new mysqli($servername, $username, $password, $dbname);
      if ($connection->connect_error) {
          die("Connection failed: " . $connection->connect_error);
      }

      $query = "SELECT name FROM location WHERE location_type=0";
      $results = $connection->query($query);
    ?>
  </head>
  <body>
    <div class="container divstyle">
      <form action="##" method="post">
        <div class="form-group">
          <select class="form-control" id="country" name="country">
            <?php while($result = $results->fetch_assoc()){ $i=$i+1; ?>
            <option value="<?php echo $i; ?>"><?php echo $result['name'] ?></option>
            <?php } ?>
          </select>
        </div>
        <div class="form-group">
          <select class="form-control" name="state" id="state"></select>
        </div>
        <div class="form-group">
          <select class="form-control" name="city" id="city"></select>
        </div>
      </form>
    </div>
  </body>
</html>
