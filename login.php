<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/styles.css">
    <style>
        body {
        background-image: url("css/new.jpg");
        background-size: cover;
        }
        .form-container {
            text-align: center;
            padding: 1%;
        }
        .headline-box {
            display: inline-block;
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            margin-top: 1%;
            margin-bottom:1%;
        }
        .headline-box h1 {
            color: darkslategray;
            font-size: 36px;
            font-family: Arial;
            margin: 0;
        }
    </style>
</head>
<body>
<div class ="form-container">
    <div class="headline-box">
        <h1>Dalhousie Food-Services</h1>
    </div>
    <form action="loginconnect.php" method="post" class="form-column">
        <img src="css/new1.jpg" alt="Image not found"/>
        <h3>Login Now</h3>
        <input type="text" name="email" placeholder="Please enter email" class="box"><br>
        <input type="password" name="password" placeholder="Please enter password"  style="padding:1.69%" class="box"><br>
        <input type="submit" value="Login" class="btn_1"><br>
        <p>Don't have an account? <a href="register.php">Register Now</a></p>
    </form>
</div>
</body>
</html>