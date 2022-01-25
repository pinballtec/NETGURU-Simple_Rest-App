Good afternoon, unfortunately I have to send such a version of the project. 

I was unable to dockerize due to django written in version 4 (docker supports 3.2)

Also, I could not send a more up-to-date version due to the fact that after all the attempts to put the project in docker, 
all versions on my computer were broken and the project did not work correctly.

I apologize and send this version

1)  api/v1/api_app/car/create/ - car creation page 

2)  api/v1/api_app/car/rating/<int:pk>/ - adding a car rating

3)  api/v1/api_app/car/list/ - view all created cars

4)  api/v1/car/detail/<int:pk>/ - the ability to edit and delete cars added earlier

Also added the ability to login and register in the application

5) api/v1/log-in/ - login 

6) ^auth/ - registration

Тhe application also has a permission system(IsOwnerOrReadOnly)
