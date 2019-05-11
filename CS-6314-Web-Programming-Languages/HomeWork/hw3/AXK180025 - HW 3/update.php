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

    if(isset($_POST['country'])){
        $query = "SELECT location_id, name FROM location WHERE location_type=1 AND parent_id=".$_POST['country'];
        $results = $connection->query($query);
        while($result = $results->fetch_assoc()){
            $state[] =  array("name" => $result['name'],
                              "id" => $result['location_id']);
        }
        $_POST['country'] = null;
        echo json_encode($state);
    }

    if(isset($_POST['state'])) {
        $query = "SELECT location_id, name FROM location WHERE location_type=2 AND parent_id=" . $_POST['state'];
        $results = $connection->query($query);
        while ($result = $results->fetch_assoc()) {
            $city[] = array("name" => $result['name'],
                            "id" => $result['location_id']);
        }
        $_POST['state'] = null;
         echo json_encode($city);
    }
?>