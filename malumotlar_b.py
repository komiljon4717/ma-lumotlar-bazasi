
import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="ali",
      passwd="123456789",
      database="DANG"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE w_20 (ID int unsigned auto_increment primary key, Student_name VARCHAR(25), student_score int(3) )")
# mycursor.execute("SHOW TABLES")
#
# mycursor.execute("INSERT INTO w_20 (Student_name, student_score) VALUES ('Olphert', 84)")
# mydb.commit()
mycursor.execute("select Student_name from w_20 where student_score=(select max(student_score) from w_20)")
all_data = mycursor.fetchall()
print(all_data)