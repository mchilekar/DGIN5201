
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="successful-checkin.js"></script>
  <meta http-equiv="refresh" content="30">
  <script>
    $(document).ready(function(){
        $("#successbreak").hide();
        $("#successlunch").hide();
        $("#successdinner").hide();


    });
    </script>
</head>
    <title>Home</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
<br>
<form action = "" method = "POST">
    <div class ="form-container-2">
        <div class="jumbotron">
            <p style="text-align: center; color: darkolivegreen; font-size: 40px;">Today's Menu</p>
            <a id="logout" style="text-align: center; font-size: 20px;" href = "templates/logout.php">Logout</a>
            <p id = "successbreak" style="text-align: center">Dear User, You have successfully checked in for Breakfast </p>
            <p id = "successlunch" style="text-align: center">Dear User, You have successfully checked in for Lunch </p>
            <p id = "successdinner" style="text-align: center">Dear User, You have successfully checked in for Dinner </p>
            <div class="well" id="breakfast" style="width: 80%;margin: auto;">    
                <h3>Breakfast</h3>   
                <h4>Mon-Sun 7:30 AM - 10:00 AM</h4>      
                <ul>
                    <li>Banana Muffin</li>
                    <li>Double Chocolate Muffin</li>
                    <li>Oatmeal Apple Muffin</li> 
                    <li>Chocolate Banana Protein Smoothie</li> 
                    <li>Bacon Hash Brown Omelette Bite</li>
                    <li>Hard Cooked Egg</li>
                    <li>Scrambled Egg</li>
                    <li>Hash Brown</li>
                    <li>Turkey Breakfast Sausage</li>
                    <li>Fried Eggs</li>  
                    <li>Apple cinnamon baked oatmeal</li>
                    <li>Basmati Rice</li>
                    <li>Tex Mex Blackbeans</li>        
                </ul>  
                <div class = "well" style="width: 80%;margin: auto;" >
                <label for= "Order"> Order Type </label>
                <br>
                <input type="radio" id="halal" class="get_value" name="radio" value="halal">
                <label for="halal"> Halal</label><br>
                <input type="radio" id="veg" class="get_value" name="radio" value="veg">
                <label for="veg"> Vegeterian</label><br>
                <input type="radio" id="vegan" class="get_value" name="radio" value="vegan">
                <label for="vegan"> Vegan</label><br>
                <input type="radio" id="nonveg"  class="get_value" name="radio" value="nonveg">
                <label for="nonveg"> Non-Vegetrian</label><br>
                <input type="radio" id="gluten" class="get_value" name="radio" value="gluten">
                <label for="gluten"> Gluten free</label>
            </div>             
                <!-- <a  class="btn btn-info" id="brkfstcheckin" role="button">Check-in</a> -->
                <button type="button" class="btn btn-primary" id="breakfastcheckin" onclick="connect()">Check-in</button>
            </div> 
            <div class="well" id="lunch" style="width: 80%; margin: auto;">    
                <h3>Lunch</h3>  
                <h4>Mon-Sun 11:30 AM - 2:00 AM</h4> 
                <ul>    
                <li>Banana Muffin</li>
                        <li>Double Chocolate Muffin</li>
                        <li>Oatmeal Apple Muffin</li> 
                        <li>Chocolate Banana Protein Smoothie</li> 
                        <li>Bacon Hash Brown Omelette Bite</li>
                        <li>Hard Cooked Egg</li>
                        <li>Scrambled Egg</li>
                </ul>
                <div class = "well" style="width: 80%; margin: auto;" >
                <label for= "Order"> Order Type </label>
                <br>
                <input type="radio" id="halal" class="get_value" name="radio" value="halal">
                <label for="halal"> Halal</label><br>
                <input type="radio" id="veg" class="get_value" name="radio" value="veg">
                <label for="veg"> Vegeterian</label><br>
                <input type="radio" id="vegan" class="get_value" name="radio" value="vegan">
                <label for="vegan"> Vegan</label><br>
                <input type="radio" id="nonveg"  class="get_value" name="radio" value="nonveg">
                <label for="nonveg"> Non-Vegetrian</label><br>
                <input type="radio" id="gluten" class="get_value" name="radio" value="gluten">
                <label for="gluten"> Gluten free</label>
            </div>
                <button type="button" class="btn btn-primary" id="lunchcheckin" onclick="connectlunch()">Check-in</button>
            </div> 
            <div class="well" id="dinner" style="width: 80%; margin: auto;">    
                <h3>Dinner</h3>   
                <h4>Mon-Sun 4:30 AM - 9:00 AM</h4>    
                <ul>
                <li>Chocolate Banana Protein Smoothie</li> 
                        <li>Bacon Hash Brown Omelette Bite</li>
                        <li>Hard Cooked Egg</li>
                        <li>Scrambled Egg</li>
                </ul>
                <div class = "well" style="width: 80%; margin: auto;" >
                <label for= "Order"> Order Type </label>
                <br>
                <input type="radio" id="halal" class="get_value" name="radio" value="halal">
                <label for="halal"> Halal</label><br>
                <input type="radio" id="veg" class="get_value" name="radio" value="veg">
                <label for="veg"> Vegeterian</label><br>
                <input type="radio" id="vegan" class="get_value" name="radio" value="vegan">
                <label for="vegan"> Vegan</label><br>
                <input type="radio" id="nonveg"  class="get_value" name="radio" value="nonveg">
                <label for="nonveg"> Non-Vegetrian</label><br>
                <input type="radio" id="gluten" class="get_value" name="radio" value="gluten">
                <label for="gluten"> Gluten free</label>
            </div>
                <button type="button" class="btn btn-primary" id="dinnercheckin" onclick="connectdinner()">Check-in</button>
            </div>  
            
        </div>

    </div>
</form>
    
</body>
</html>