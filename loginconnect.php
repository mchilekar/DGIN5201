<?php

$is_invalid = false;

if ($_SERVER["REQUEST_METHOD"] === "POST") {
   
    $mysqli = require "database.php";    
    $sql = sprintf("SELECT * FROM user
                    WHERE username = '%s'",
                   $mysqli->real_escape_string($_POST["email"]));
    
    
    $result = $mysqli->query($sql);
    
    $user = $result->fetch_assoc();
    
    if ($user) {

        if (password_verify($_POST["password"], $user["userpassword"])){
         
            session_start();

            session_regenerate_id();
            echo "Inside";
            $_SESSION["user_id"] = $user["username"];   
            $sql =  "SELECT ID FROM user WHERE username = ?";
            $stmt = $mysqli->stmt_init();
             if(!$stmt->prepare($sql) ) {
              die("SQL error:  " . $mysqli->error);
            }

            $stmt->bind_param("s", $user["username"]);
            $stmt->execute();      
            $result = mysqli_stmt_get_result($stmt);
            $row = mysqli_fetch_assoc($result); 
            echo $row["ID"];
           
            if (substr($row["ID"], 0, 1) === "B"){
                
                  header("Location: index.php");
             }
             else{
                //header("Location: employee.php");  
                header("Location: http://3.138.109.137/:5000/employee");  
                
            }
            
            exit;
        }
    }
    
    $is_invalid = true;
        }


?>
