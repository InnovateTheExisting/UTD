<html>


<head>
    <title>Flickr Search</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

    <style type="text/css">
        .container{
            padding: 10px;
            width: 100%;

        }

        .data{
            margin: 5px;
            width: 100px;
            height: 100px;
        }

        .form{
            text-align: center;
        }
    </style>
<?php
/**
 * Created by PhpStorm.
 * User: dchha
 * Date: 4/9/2019
 * Time: 7:22 PM
 */

require_once('flickr.php');
if(isset($_POST['submit'])){
    $s_val=$_POST['search'];
    if($s_val!="") {
        $Flickr = new flickr('78dc2b13d9cc1127139a1aa12bf9fcc6');
        $data = $Flickr->search($s_val);
    }
}

?>

</head>

<body>

<div class="container">
    <h1 class="form">Flickr Image Search</h1>
    <form class="form" action="index.php" method="POST">
        <input type="search" name="search" placeholder="Search">
        <button class="btn btn-success" type="submit" name="submit">Search</button>
        <button class="btn btn-primary" type="reset" name="submit">Reset</button>
    </form>

    <div class="form">
    <?php
    if(isset($data)) {
        echo "Search Text: " . $s_val;
    }
        ?>
    </div>

    <div>
        <?php
        if(isset($data)) {
            foreach ($data['photos']['photo'] as $photo) {
                /*
                * https://www.flickr.com/photos/{user-id}/{photo-id} - individual photo
                */
                echo '<a  href="https://www.flickr.com/photos/' . $photo["owner"] . '/' . $photo["id"] . '" target="_blank"><img class="data" src="' . 'http://farm' . $photo["farm"] . '.static.flickr.com/' . $photo["server"] . '/' . $photo["id"] . '_' . $photo["secret"] . '_t.jpg"></a>';
            }
        }
        ?>
    </div>

</div>




</body>

</html>
