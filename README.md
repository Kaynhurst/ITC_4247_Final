Task Manager Instructions :

1. Download repository into a safe folder.
2. Open the web-app directory.
3. Run the following commands
   docker-compose build.
   docker-compose up (If you are using Docker Desktop you can use the prefix "-d" to have a detached container independant from the terminal )
   
4. Wait for the container to initialize.
5. If there are any issues with the web_app-container not being able to start, wait for the container-pg to fully initialize as it houses the database.
6. Navigate to the http://localhost:8000 to access the web app.

7. You can also navigate to the http://localhost:5050/login , to access the pgAdmin in order see the database directly.


The following are the credentials for each localhost

  - localhost:8000 Credentials :
     -  admin : root (Super user)
     -  mikes : mike123
     -  kpap : kostas123
     -  johnp : john123
  
  - localhost:5050
      - admin@admin.com  : root
      - To access the postgres database use the following steps:
            - Add server
            - Add a name for your choice
            - Navigate to connection and enter the databse IP ---> This is commonly found via the terminal commadn --> docker inspect container-pg. This should yield the database IP. Most of the time the IP associated is 172.18.0.2 however this is subject to change.
            - add 'root' as the password in the prompt.
            - The server connection is completed.

To add new or edit Tasks use the following format :
    {
    "task" : 'Task Name',
    "description" : 'Task Description',
    "completed" : true / false (depending on prefrence)
    }

Additional Notes : 
   - If an error relating to the rest_api_tasks_db occurs, try restarting the web_app-container after waiting for the container-pg to fully initialize.
   - If there are any issues regarding the Docker, remove the Task Manager Secure version from the folder (This is untested and possible unintentional functionality)
   - Should you reach an error url, you can easily redirect to the intended web service by going to the http://localhost:8000/api/ link.

