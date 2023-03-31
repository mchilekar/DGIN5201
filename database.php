<!-- <?php

// $dbServerName = "db.cs.dal.ca";
// $dbUserName = "chilekar";
// $dbPassword = "JHrGy3W7i9UiNmosgAfPs7tFd";
// $dbName = "mayuri";

// $mysqli = new mysqli($dbServerName, $dbUserName, $dbPassword, $dbName);



// if ($mysqli->connect_errno){
//     die("Connection error: " . $mysqli->connect_error);
// }


// return $mysqli;

?> -->

<?php
$servername = "db.cs.dal.ca";
$username = "chilekar";
$password = "TKZ7VWVFoSqP9qyyxVwAHT9pZ";
$database = "chilekar";

// Create connection
$mysqli = new mysqli($servername, $username, $password, $database);

// Check connection
if ($mysqli->connect_error) {
  die("Connection failed: " . $mysqli->connect_error);
}
return $mysqli;
?>
