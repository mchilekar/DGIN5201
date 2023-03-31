from flask import Flask, render_template, request,redirect, jsonify, abort
from flask_mysqldb import MySQL
# import yaml
from flask_cors import CORS, cross_origin
import mysql.connector
from datetime import date


app = Flask(__name__, template_folder='templates')
CORS(app,support_credentials=True)


# db = yaml.safe_load(open('C:/xampp/htdocs/Digital Transformation/Employee/db.yaml'))
# app.config['MYSQL_HOST'] = 'db.cs.dal.ca' #db['mysql_host']
# app.config['MYSQL_USER'] =  'chilekar' #db['mysql_user']
# app.config['MYSQL_PASSWORD'] = 'WVxfa7JN9hGiuR3UgoqRH7nNK' #db['mysql_password']
# app.config['MYSQL_DB'] = 'chilekar' #db['mysql_db']

connection = mysql.connector.connect(host='db.cs.dal.ca',
                                         database='chilekar',
                                         user='chilekar',
                                         password='TKZ7VWVFoSqP9qyyxVwAHT9pZ')

#mysql = MySQL(app)
#cursor = mysql.connect.cursor()

@app.route('/update-click-count', methods=['POST'])
@cross_origin(supports_credentials=True)
def update_click_count():
    try:
        try:
            cursor = connection.cursor()
            #cursor = mysql.connection.cursor()
            data = request.get_json()
            today = date.today()
            item_id = data['item_id']   
            cursor.execute("SELECT * FROM breakfast WHERE Date = CURDATE();")
            if cursor.fetchone() is not None:
                sql = "Select breakfastcount from breakfast where Date = %s;"
                cursor.execute(sql, (today,))
                result = cursor.fetchall()
                print("Breakfast",result[0][0]) 
                query = "Update breakfast set breakfastcount = %s where Date = %s;"
                record = (result[0][0]+1,today)
                cursor.execute(query, record) 
                output = insertbreakfast()
                               
            else:
                mySql_insert_query = "INSERT INTO breakfast (breakfastcount,Date,halal,veg,vegan,nonveg,gluten) VALUES ( %s, %s,%s, %s, %s, %s,%s);"
                record = (1,today,0,0,0,0,0)
                cursor.execute(mySql_insert_query, record)           
                output = insertbreakfast()

            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Laptop table")
            cursor.close()      
        except mysql.connector.Error as error:
            print("Failed to insert record into Breakfast table {}".format(error))

        return jsonify({'success': True}), 200
    except IndexError:
        return "Error", 500  
    
   

@app.route('/update-lunch-count', methods=['POST'])
@cross_origin(supports_credentials=True)
def update_lunch_count():
    try:
        try:
            cursor = connection.cursor()
            #cursor = mysql.connection.cursor()
            data = request.get_json()
            today = date.today()
            item_id = data['item_id']   
            cursor.execute("SELECT * FROM lunch WHERE Date = CURDATE();")
            if cursor.fetchone() is not None:
                sql = "Select lunchcount from lunch where Date = %s;"
                cursor.execute(sql, (today,))
                result = cursor.fetchall()
                print("Lunch",result[0][0]) 
                query = "Update lunch set lunchcount = %s where Date = %s;"
                record = (result[0][0]+1,today)
                cursor.execute(query, record)    
                output = insertlunch()            
            else:
                mySql_insert_query = "INSERT INTO lunch (lunchcount,Date,halal,veg,vegan,nonveg,gluten) VALUES ( %s, %s,%s, %s, %s, %s,%s);"
                record = (1,today,0,0,0,0,0)
                cursor.execute(mySql_insert_query, record)           
                output = insertlunch()
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Lunch table")
            cursor.close()        
                
        except mysql.connector.Error as error:
            print("Failed to insert record into Lunch table {}".format(error))

        return jsonify({'success': True}), 200
    except IndexError:
        return "Error", 500
  
@app.route('/update-dinner-count', methods=['POST'])
@cross_origin(supports_credentials=True)
def update_dinner_count():
    try:
        try:
            cursor = connection.cursor()
            #cursor = mysql.connection.cursor()
            data = request.get_json()
            today = date.today()
            item_id = data['item_id']   
            cursor.execute("SELECT * FROM dinner WHERE Date = CURDATE();")
            print("Here inside dinner funciton")
            if cursor.fetchone() is not None:
                sql = "Select dinnercount from dinner where Date = %s;"
                cursor.execute(sql, (today,))
                result = cursor.fetchall()
                print("Dinner",result[0][0]) 
                query = "Update dinner set dinnercount = %s where Date = %s;"
                record = (result[0][0]+1,today)
                cursor.execute(query, record)    
                output = insertdinner()            
            else:
                mySql_insert_query = "INSERT INTO dinner (dinnercount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s,%s, %s, %s, %s,%s);"
                record = (1,today,0,0,0,0,0)
                cursor.execute(mySql_insert_query, record)           
                output = insertdinner()
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Dinner table")
            cursor.close()    
        except mysql.connector.Error as error:
            print("Failed to insert record into dinner table {}".format(error))

        return jsonify({'success': True}), 200
    except IndexError:
        return "Error", 500 
    

# @app.route('/employee-dashboard', methods=['GET'])   
# @cross_origin()
# def employee_dashboard():
#     try:
#         today = date.today()
#         cursor = connection.cursor();
#         #data = request.get_json()
#         #item_id = data['item_id'] 
#         #print("Item ID",item_id)  
#         #if item_id == "breakfastdata":
#         cursor.execute("SELECT breakfastcount,halal,veg,vegan,nonveg,gluten FROM breakfast WHERE Date = CURDATE();")
#         result = cursor.fetchall()
#         print(result)
       
#        # return render_template('templates/Bcount1.html',count = result1,halal = result2, veg=result3, vegan=result4,nonveg = result5, gluten = result6)  
#         return render_template('templates/Bcount.php', results = result)
#     except IndexError:
#         return "No checkin data present", 500 
    
@app.route('/insertbreakfast', methods=['POST'])
@cross_origin(supports_credentials=True)
def insertbreakfast():
    try:
        try:
            cursor = connection.cursor()
            #cursor = mysql.connection.cursor()
            data = request.get_json()
            today = date.today()
            item_id = data['order']   
            print("Inisde Insert",item_id)
            cursor.execute("SELECT * FROM breakfast WHERE Date = CURDATE();")
            if cursor.fetchone() is not None:
                if item_id == "halal":
                    sql = "Select halal from breakfast where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("halal",result[0][0]) 
                    query = "Update breakfast set halal = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)   
                elif item_id == "veg":
                    sql = "Select veg from breakfast where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("veg",result[0][0]) 
                    query = "Update breakfast set veg = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)
                elif item_id == "vegan":
                    sql = "Select vegan from breakfast where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("vegan",result[0][0]) 
                    query = "Update breakfast set vegan = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)  
                elif item_id == "nonveg":
                    sql = "Select nonveg from breakfast where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("nonveg",result[0][0]) 
                    query = "Update breakfast set nonveg = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)
                else:
                    sql = "Select gluten from breakfast where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("gluten",result[0][0]) 
                    query = "Update breakfast set gluten = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)

            else:
                if item_id == "halal":
                    mySql_insert_query = "INSERT INTO breakfast (breakfastcount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s,  %s, %s, %s, %s, %s,%s);"
                    record = (0,today,1,0,0,0,0)
                    cursor.execute(mySql_insert_query, record)      
                elif item_id == "veg":
                    mySql_insert_query = "INSERT INTO breakfast (breakfastcount, Date,halal,veg,vegan,nonveg,gluten) VALUES ( %s, %s, %s, %s, %s, %s,%s);"
                    record = (0,today,0,1,0,0,0)
                    cursor.execute(mySql_insert_query, record)  
                elif item_id == "vegan":
                    mySql_insert_query = "INSERT INTO breakfast (breakfastcount, Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s,%s);"
                    record = (0,today,0,0,1,0,0)
                    cursor.execute(mySql_insert_query, record)
                elif item_id == "nonveg":
                    mySql_insert_query = "INSERT INTO breakfast (breakfastcount, Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s,%s);"
                    record = (0,today,0,0,0,1,0)
                    cursor.execute(mySql_insert_query, record)   
                else:
                    mySql_insert_query = "INSERT INTO breakfast (breakfastcount, Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s,%s);"
                    record = (0,today,0,0,0,0,1)
                    cursor.execute(mySql_insert_query, record)

           
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Breakfast table")
            cursor.close() 

        except mysql.connector.Error as error:
            print("Failed to insert record into breakfast table {}".format(error))

        return jsonify({'success': True}), 200
    
    except:
        return "Error", 500 

@app.route('/insertlunch', methods=['POST'])
@cross_origin(supports_credentials=True)
def insertlunch():
    try:
        try:
            cursor = connection.cursor()
            #cursor = mysql.connection.cursor()
            data = request.get_json()
            today = date.today()
            item_id = data['order']   
            print("Inisde Insert")
            cursor.execute("SELECT * FROM lunch WHERE Date = CURDATE();")
            if cursor.fetchone() is not None:
                if item_id == "halal":
                    sql = "Select halal from lunch where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("halal",result[0][0]) 
                    query = "Update lunch set halal = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)   
                elif item_id == "veg":
                    sql = "Select veg from lunch where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("veg",result[0][0]) 
                    query = "Update lunch set veg = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)
                elif item_id == "vegan":
                    sql = "Select vegan from lunch where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("vegan",result[0][0]) 
                    query = "Update lunch set vegan = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)  
                elif item_id == "nonveg":
                    sql = "Select nonveg from lunch where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("nonveg",result[0][0]) 
                    query = "Update lunch set nonveg = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)
                else:
                    sql = "Select gluten from lunch where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("gluten",result[0][0]) 
                    query = "Update lunch set gluten = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)

            else:
                if item_id == "halal":
                    mySql_insert_query = "INSERT INTO lunch (lunchcount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,1,0,0,0,0)
                    cursor.execute(mySql_insert_query, record)      
                elif item_id == "veg":
                    mySql_insert_query = "INSERT INTO lunch (lunchcount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,0,1,0,0,0)
                    cursor.execute(mySql_insert_query, record)  
                elif item_id == "vegan":
                    mySql_insert_query = "INSERT INTO lunch (lunchcount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,0,0,1,0,0)
                    cursor.execute(mySql_insert_query, record)
                elif item_id == "nonveg":
                    mySql_insert_query = "INSERT INTO lunch (lunchcount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,0,0,0,1,0)
                    cursor.execute(mySql_insert_query, record)   
                else:
                    mySql_insert_query = "INSERT INTO lunch (lunchcount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,0,0,0,0,1)
                    cursor.execute(mySql_insert_query, record)

           
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Lunch table")
            cursor.close() 

        except mysql.connector.Error as error:
            print("Failed to insert record into lunch table {}".format(error))

        return jsonify({'success': True}), 200
    
    except:
        return "Error", 500 

@app.route('/insertdinner', methods=['POST'])
@cross_origin(supports_credentials=True)
def insertdinner():
    try:
        try:
            cursor = connection.cursor()
            #cursor = mysql.connection.cursor()
            data = request.get_json()
            today = date.today()
            item_id = data['order']   
            print("Inisde Insert")
            cursor.execute("SELECT * FROM dinner WHERE Date = CURDATE();")
            if cursor.fetchone() is not None:
                if item_id == "halal":
                    sql = "Select halal from dinner where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("halal",result[0][0]) 
                    query = "Update dinner set halal = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)   
                elif item_id == "veg":
                    sql = "Select veg from dinner where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("veg",result[0][0]) 
                    query = "Update dinner set veg = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)
                elif item_id == "vegan":
                    sql = "Select vegan from dinner where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("vegan",result[0][0]) 
                    query = "Update dinner set vegan = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)  
                elif item_id == "nonveg":
                    sql = "Select nonveg from dinner where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("nonveg",result[0][0]) 
                    query = "Update dinner set nonveg = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)
                else:
                    sql = "Select gluten from dinner where Date = %s;"
                    cursor.execute(sql, (today,))
                    result = cursor.fetchall()
                    print("gluten",result[0][0]) 
                    query = "Update dinner set gluten = %s where Date = %s;"
                    record = (result[0][0]+1,today)
                    cursor.execute(query, record)

            else:
                if item_id == "halal":
                    mySql_insert_query = "INSERT INTO dinner (dinnercount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,1,0,0,0,0)
                    cursor.execute(mySql_insert_query, record)      
                elif item_id == "veg":
                    mySql_insert_query = "INSERT INTO dinner (dinnercount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,0,1,0,0,0)
                    cursor.execute(mySql_insert_query, record)  
                elif item_id == "vegan":
                    mySql_insert_query = "INSERT INTO dinner (dinnercount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,0,0,1,0,0)
                    cursor.execute(mySql_insert_query, record)
                elif item_id == "nonveg":
                    mySql_insert_query = "INSERT INTO dinner (dinnercount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,0,0,0,1,0)
                    cursor.execute(mySql_insert_query, record)   
                else:
                    mySql_insert_query = "INSERT INTO dinner (dinnercount,Date,halal,veg,vegan,nonveg,gluten) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);"
                    record = (1,today,0,0,0,0,1)
                    cursor.execute(mySql_insert_query, record)

           
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Dinner table")
            cursor.close() 

        except mysql.connector.Error as error:
            print("Failed to insert record into dinner table {}".format(error))

        return jsonify({'success': True}), 200
    
    except:
        return "Error", 500 


@app.route('/employee', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def employee():
    cursor = connection.cursor()           
    today = date.today()
    cursor.execute("SELECT * FROM dinner WHERE Date = CURDATE();")
    if cursor.fetchone() is not None:
        sql = "Select dinnercount,halal,veg,vegan,nonveg,gluten from dinner where Date = %s;"
        cursor.execute(sql, (today,))
        result = cursor.fetchall()
        count = result[0][0]
        halal = result[0][1]
        veg = result[0][2]
        vegan = result[0][3]
        nonveg = result[0][4]
        gluten = result[0][5]
        print("Breakfast",result)
        return render_template("Dcount.php", count=count, halal=halal, veg=veg,vegan=vegan, nonveg=nonveg,gluten=gluten)
    
    else:
        return"Record not found"
        
    




if __name__ == '__main__':
    app.run(debug=True)
