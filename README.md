# API_Immfly
API_Immfly


Se debe ir al directorio que contiene el contenido docker en /API_Docker/Project_Immfly
y ejecutar 

	 sudo docker build .

para construir la imagen.
Luego generaremos los contenedores de esa imagen

	sudo docker-compose up -d

Tambien hay que crear la base de datos y sos roles

 	docker exec -it project_immfly_db_1 psql -U postgres -d template1

y dentro crear roles y base de datos:

	CREATE ROLE immfly PASSWORD 'immfly';
	ALTER ROLE immfly WITH createdb;
	ALTER ROLE immfly WITH login;
	CREATE DATABASE immfly;
	ALTER database immfly owner to  immfly;
	
Luego realizamos la migracion a la base de datos:

	docker exec -it project_immfly_web_1 python3 manage.py migrate

Hacemos una importacion de la base de datos con canales y contenidos ajustados a los requerimientos
	
	docker exec -i project_immfly_db_1 psql -U immfly immfly < pg_immfly.sql

Ya estariamos en condiciones de ejecutar el servidor web

#Lista de todos los canales que no tienen hijos	

	http://127.0.0.1:8000/api_Immfly/channels/

#Lista de subcanales de un canal especifico

	http://127.0.0.1:8000/api_Immfly/channel/7

#Lista de contenidos de un canal especifico

	http://127.0.0.1:8000/api_Immfly/contents/7

###Para ejecutar la funcion de rating:

	docker exec -it project_immfly_web_1 python3 manage.py ratings

###Para ejecutar los test unitarios:

	docker exec -it project_immfly_web_1 python3 manage.py test
