# About this program
This project requires a Pytohn 3.X version and a database called mibase with 3 tables. If you want to change the databases, you need specificate the changes in each one python scripts that need to connect with the database. But if you wanna try with the default specifications, just create a database "mibase" with the follow tables:

The first table "users":
id Primary	int(11),
user_name	varchar(12),
user_pass	varchar(6),
first_name	varchar(30),
last_name	varchar(30),
age	int(11),
img_profile	blob
  
The second table "ingresos":
  user	varchar(30),
	year	int(4),
	january	int(10),
	february	int(10),
	march	int(10),
	april	int(10),
	may	int(10),
	june	int(10),
	july	int(10),
	august	int(10),
	september	int(10),
	october	int(10),
	november	int(10),
	december	int(10)
  
The third table "gastos":
  user	varchar(30),
	year	int(4),
	january	int(10),
	february	int(10),
	march	int(10),
	april	int(10),
	may	int(10),
	june	int(10),
	july	int(10),
	august	int(10),
	september	int(10),
	october	int(10),
	november	int(10),
	december	int(10)
  
  # NOTE
  ## Don't forget to activate your serv to run this app correctly!
