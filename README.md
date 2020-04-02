# python-docker-example

This repository demonstrates how to create a docker image for simple python project.


## Steps to build Docker image:

1. Clone the repository.

    ```git
    git clone https://github.com/sagar-rathod/python-docker-example.git
    ```

2. Navigate to <strong>python-docker-example</strong> directory.
3. Run the following command:

    ```bash
    docker build --tag python-docker-example .
   ```
   
4. After successful creation of docker image with above command, you can check <strong>python-docker-example</strong> appears in your list of docker images.

    ```bash
    docker image ls 
   ```

## Run python script inside docker container:

1. Run the following command to see help message:

    ```docker
   docker run --rm --name pde python-docker-example 
   ```
    Output:
    ```docker
   NAME
       calc.py
   
   SYNOPSIS
       calc.py COMMAND
   
   COMMANDS
       COMMAND is one of the following:
   
        add
   
        mean
   
        mult
   
        std_dev
   
        sub
   
        var 
   ```

2. Try out one of above different command as follows:

    ```bash
    docker run --rm --name pde python-docker-example  python ./example/calc.py add 1 2 3 4 5
   ```
   
   ```bash
   docker run --rm --name pde python-docker-example  python ./example/calc.py mult 1 2 3 4 5
   ```
