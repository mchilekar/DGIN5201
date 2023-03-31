<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body style="background-image: url('css/new.jpg');">
<div class ="form-container-3">
    <form action="process-signup.php" method="post" class="form-column-2">
        <h3>Dal Food Services Employee Sign-up</h3>
        <input type="text" name="firstName" placeholder="Please enter first name" class="box"><br>
        <input type="text" name="lastName" placeholder="Please enter last name" class="box"><br>
        <input type="email" name="email" placeholder="Please enter email" class="box"><br>
        <input type="employee" name="employeeID" maxlength="9" placeholder="Please enter Employee ID or Student ID" class="box"><br>
        <input type="password" name="password" placeholder="Please enter password" class="box"><br>
        <input type="password" name="confirm" placeholder="Please confirm password" class="box"><br>
        <input type="submit" value="Register" class="btn"><br>
        <p>Already have an account? <a href="login.php">Login Now</a></p>
    </form>
</div>
</body>
</html>