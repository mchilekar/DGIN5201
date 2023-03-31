<?php

if (empty($_POST["firstName"])){
    die("First Name is required");
}

if (empty($_POST["lastName"])){
    die("Last Name is required");
}

if (empty($_POST["email"])){
    die("Name is required");
}
if (empty($_POST["employeeID"])){
    die("Employee ID is required");
}

if (empty($_POST["password"])){
    die("Password is required");
}

if ($_POST["password"] !== $_POST["confirm"]){
    die("Passwords must match");
}

$password_hash = password_hash($_POST["password"], PASSWORD_DEFAULT);
$uniqueID =  $_POST["employeeID"];
$username =  $_POST["email"];
$mysqli = include "database.php";

if (substr($uniqueID, 0, 1) === "B") {

    $sql = "INSERT INTO student_data(firstName, lastName, email, loginPassword,studentID)
    VALUES (?, ?, ?, ?, ?)";
    $sql1 = "INSERT INTO user(username, userpassword, ID)
    VALUES (?, ?,?)";

}
else {
    $sql = "INSERT INTO user_form (firstName, lastName, email, loginPassword, employeeID)
    VALUES (?, ?, ?, ?, ?)";
    $sql1 = "INSERT INTO user (username, userpassword, ID)
    VALUES (?, ?, ?)";
}

$stmt = $mysqli->stmt_init();


if(!$stmt->prepare($sql) ) {
    die("SQL error:  " . $mysqli->error);
}

$stmt->bind_param("sssss", $_POST["firstName"], $_POST["lastName"], $_POST["email"], $password_hash, $_POST["employeeID"]);
$stmt->execute();

$stmt1 = $mysqli->stmt_init();
if(!$stmt1->prepare($sql1) ) {
    die("SQL error:  " . $mysqli->error);
}

$stmt1->bind_param("sss", $_POST["email"] , $password_hash, $_POST["employeeID"]);
$stmt1->execute();

header("Location: signup-success.php");
exit;

?>