<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <link rel="stylesheet" href="css/styles.css">
    <style>
        
table {
    border-collapse: separate;
    border-spacing: 0;
    margin: 0 auto;
    background-color: rgba(255, 255, 255, 0.5);
    font-family: 'Open Sans', sans-serif;
    font-size: 18px;
}

table, th, td {
    border: 1px solid black;
}

th, td {
    padding: 12px;
}

th:first-child,
td:first-child {
    border-top-left-radius: 10px;
}

th:last-child,
td:last-child {
    border-top-right-radius: 10px;
}

tr:last-child td:first-child {
    border-bottom-left-radius: 10px;
}

tr:last-child td:last-child {
    border-bottom-right-radius: 10px;
}


html, body {
    height: 100%;
    background: linear-gradient(to bottom right, lightblue, lightgreen);
}
.jumbotron-1 {
    /* background: linear-gradient(to bottom right, lightblue, lightgreen); */
    opacity: 0.8;
    min-height: 100%;
}
.jumbotron-1 h1 {
    margin-left: 465px;
    font-family: 'Open Sans', sans-serif;
}

tr:hover {
    background-color: #f5f5f5;
}
    </style>  
</head>
<body>

<div class ="form-container-4">
<div class="jumbotron-1">
<!-- <a id="logout" style="text-align: center; font-size: 20px;" href = "templates/logout.php">Logout</a> -->
     <table border=1>
        <h1>Today's Dinner Count</h1>
        <tr>
            <th>Meal</th>
            <th> Students count</th>
        </tr>
        <tr>            
            <td>Dinner</td>
            <td>{{count}}</td>
        </tr>
        <tr>
            <td>Halal</td>
            <td>{{halal}}</td>
        </tr>
        <tr>
            <td>Vegeterian</td>
            <td>{{veg}}</td>
        </tr>
        <tr>
            <td>Vegan</td>
            <td>{{vegan}}</td>
        </tr>
        <tr>
            <td>Non-Veg</td>
            <td>{{nonveg}}</td>
        </tr>
        <tr>
            <td>Gluten free</td>
            <td>{{gluten}}</td>
        </tr> 

</table>
</div>
</div>
</body>
</html>