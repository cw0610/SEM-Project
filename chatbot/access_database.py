import mysql.connector

class SQL_Database():

    def get_output(attribute,key,key_attribute):

        output = []
        try:
            mydb = mysql.connector.connect(
              host="localhost",
              port=3307,
              user="root",
              passwd="",
              auth_plugin='mysql_native_password',
              database="carrental"
            )

            mycursor = mydb.cursor()
            if attribute == "id" or attribute == "VehiclesBrand" or key_attribute == "id" or key_attribute == "VehiclesBrand":
                sql = f"SELECT donottrytohack FROM tblvehicles"
            else:
                if key_attribute is None:
                    sql = f"SELECT tblvehicles.VehiclesTitle, tblbrands.BrandName, tblvehicles.PricePerDay, tblvehicles.FuelType, tblvehicles.ModelYear, tblvehicles.SeatingCapacity  FROM tblvehicles JOIN tblbrands ON tblvehicles.VehiclesBrand = tblbrands.id WHERE tblvehicles.VehiclesTitle LIKE '%{key}%' OR tblbrands.BrandName LIKE '%{key}%' OR tblvehicles.PricePerDay LIKE '%{key}%' OR tblvehicles.FuelType LIKE '%{key}%' OR tblvehicles.ModelYear LIKE '%{key}%' OR tblvehicles.SeatingCapacity LIKE '%{key}%'"
                elif attribute == key_attribute and attribute != "BrandName":
                    sql = f"SELECT {attribute} FROM tblvehicles WHERE {key_attribute} LIKE '%{key}%'"
                elif attribute == key_attribute and attribute == "BrandName":
                    sql = f"SELECT tblbrands.{attribute} FROM tblvehicles JOIN tblbrands ON tblvehicles.VehiclesBrand = tblbrands.id WHERE tblbrands.{key_attribute} LIKE '%{key}%'"
                elif attribute == "BrandName":
                    sql = f"SELECT tblbrands.{attribute}, tblvehicles.{key_attribute} FROM tblvehicles JOIN tblbrands ON tblvehicles.VehiclesBrand = tblbrands.id WHERE tblvehicles.{key_attribute} LIKE '%{key}%'"
                elif key_attribute == "BrandName":
                    sql = f"SELECT tblvehicles.{attribute}, tblbrands.{key_attribute} FROM tblvehicles JOIN tblbrands ON tblvehicles.VehiclesBrand = tblbrands.id WHERE tblbrands.{key_attribute} LIKE '%{key}%'"
                else:
                    sql = f"SELECT {key_attribute},{attribute} FROM tblvehicles WHERE {key_attribute} LIKE '%{key}%'"

            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            for x in myresult:
              output.append(x)

        except mysql.connector.Error as error:
          print("Failed to insert record into Laptop table {}".format(error))

        finally:
            if (mydb.is_connected()):
                mydb.close()
                print("MySQL connection is closed")

        return output

