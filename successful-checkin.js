var breakfast_cnt=0;
var lunch_cnt = 0;
var dinner_cnt = 0;



   // document.getElementById(breakfastcheckin).addEventListener('click', function() {
    async function connect(){
      $("#successbreak").hide();  
      $("#successlunch").hide();  
      $("#successdinner").hide();  
        var insert = []
        breakfast_cnt = breakfast_cnt + 1;
        console.log("breakfast"+breakfast_cnt);  
        $(".get_value").each(function(){
          if($(this).is(":checked")){
            insert.push($(this).val());
          }
        });
        //alert(insert[0])
        // insert = insert.toString();
        var raw = JSON.stringify({
        "item_id": breakfast_cnt,
        "order": insert[0],
      });

    await fetch('http://3.138.109.137:5000/update-click-count', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: raw })
      .then(response => {
        response.json().then((data) => {
            console.log(data.success);
        })
      })
      .catch(error => console.log(error))    
      //$("#submit").click();   
      $("#successbreak").show();
      //window.location.href = "successful-checkin.php";
     }

// Function call for lunch checkin
     async function connectlunch(){ 
      //alert("inside lunch")
      var insert = [];
      $("#successbreak").hide();  
      $("#successlunch").hide();  
      $("#successdinner").hide();  
      lunch_cnt = lunch_cnt + 1;
      console.log("lunch"+lunch_cnt);
      $(".get_value").each(function(){
        if($(this).is(":checked")){
          insert.push($(this).val());
        }
      });
      var raw = JSON.stringify({
        "item_id": lunch_cnt,
        "order": insert[0],
      });
      //alert("Here"+ raw)
     await fetch('http://3.138.109.137:5000/update-lunch-count', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
    },
    body: raw })
    .then(response => {
      response.json().then((data) => {
          console.log(data.success);
      })
    })
    .catch(error => console.log(error)) 
   // $("#submit").click();   
    $("#successlunch").show();      
    //window.location.href = "successful-checkin.php";
   }
   

// Function call for dinner checkin
async function connectdinner(){
  var insert = [];  
  $("#successbreak").hide();  
      $("#successlunch").hide();  
      $("#successdinner").hide();       
  dinner_cnt = dinner_cnt + 1;
  console.log("dinner"+dinner_cnt);
  $(".get_value").each(function(){
    if($(this).is(":checked")){
      insert.push($(this).val());
    }
  });
  var raw = JSON.stringify({
    "item_id": dinner_cnt,
    "order": insert[0],
  });
  //alert("Here"+ raw)
 await fetch('http://3.138.109.137:5000/update-dinner-count', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
},
body: raw })
.then(response => {
  response.json().then((data) => {
      console.log(data.success);
  })
})
.catch(error => console.log(error)) 
//$("#submit").click();     
$("#successdinner").show();    
//window.location.href = "successful-checkin.php";
}

// Function call for dinner checkin
async function submitdata(){     
  var insert = []
  
  $(".get_value").each(function(){
    if($(this).is(":checked")){
      insert.push($(this).val());
    }
  });
  
  insert = insert.toString();
  var insert_string = "checkboxvalue="+insert;
  var raw = JSON.stringify({
    "data": insert
  });
  //alert("Here"+ raw)
 await fetch('http://localhost:5000/insert', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
},
body: raw })
.then(response => {
  response.json().then((data) => {
      console.log(data.success);
  })
})
.catch(error => console.log(error))   
   
}
