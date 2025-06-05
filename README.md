# Simple Task Manager API

This is a simple REST API built with Django that manages a list of tasks stored in a local array.  
The API supports adding new tasks, marking tasks as completed, deleting tasks, and retrieving all tasks.


## Features

- **GET /api/tasks/** : Retrieve all tasks  
- **POST /api/tasks/** : Add a new task  
- **PUT /api/tasks/:id/** : Mark a task as completed  
- **DELETE /api/tasks/:id/** : Delete a task by ID  

Tasks are stored in a local in-memory array, so data will reset when the server restarts.


