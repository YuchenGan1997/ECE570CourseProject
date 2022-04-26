# ECE570CourseProject
## How to run the project
### admin app
First move to the admin folder, if you are the first time to run this app, you need to change the command in [docker-compose.yml](https://github.com/YuchenGan1997/ECE570CourseProject/blob/main/python-microservices/admin/docker-compose.yml) file
If you have already ran this app before, you can change the command in [docker-compose.yml](https://github.com/YuchenGan1997/ECE570CourseProject/blob/main/python-microservices/admin/docker-compose.yml) back to the regular command. 
And in the future running, you don't need to change anything.
Once you have changed the file, you need to run `docker-compose build` and then run `docker-compose up`.
### main app
Same as the admin app, move to the main folder, and change the command in [docker-compose.yml](https://github.com/YuchenGan1997/ECE570CourseProject/blob/main/python-microservices/main/docker-compose.yml)
Then once you changed the command you need for first run, you can run `docker-compose build` and then run `docker-compose up` to start the main app. Then in the future running, you only need to use the regular 
running command.
### react-crud frontend page
After running the two applications above, you can run the react-crud by running `npm install` and then run `npm start`.

