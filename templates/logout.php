
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <link rel="stylesheet" href="css/styles.css">

</head>
<body>

<p> You have been successfully logout! </p>

    
</body>
</html>

<?php

session_start();

session_destroy();

//header("Location:index.php");
exit;

?>