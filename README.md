### Task 
- This Project contains a main.py file which includes code to load a model from timm, and pass an image in that model to get output in json format. 
- Here no training of model is involved, but if needed, a separate ``train.py`` file could be added. 
- The requirements.txt file contains the package requirements which is used by the Dockerfile. 
- The Dockerfile contains the basic instructions in order to build an image. 
- test.sh file contains some basic tests to check whether the build runs, output is in json format or not etc. 
- Note: the final image size should preferrably be less than 1GB

### Commands Required to run the model . 

- ``docker build -t shilpi06/timm . `` 

- ``docker run shilpi06/timm --model 'resnet18' --image 'https://github.com/pytorch/hub/raw/master/images/dog.jpg'``

- It's important to define an entry point, as every argument that we pass such as --foo=bar would be given to the entrypoint, in our case python3 main.py. 

- The given link above, is a link for the image. 

- Extra Note: In order to get the image size to be less than 1GB, we can remove the cache. We can check the size of cache by running the container interactively in bash. 

- Do : ``docker run -it --entrypoint /bin/bash shilpi06/timm``, Then do: ``cd ~`` to go to root. On doing ``ls -a``, you'll see .cache . To check the size of cache, do: ``du -sh .cache/``. In order to remove this cache, we'll now modify the Dockerfile by adding an extra line: && ``&& rm -rf /root/.cache/`` . 
- In this case however, I've already modified the Dockerfile. 

- Also, note: you must specify versions for libraries in your requriements.txt file. 

### Hydra [ Work In Progress]
- Hydra is a framework developed by Facebook for elegantly configuring complex applications. One of Hydra's primary features is allowes you to dynamically create a hierarchical configuration by composing multiple config files and overriding them from the command line. It's beneficial for applications that have complex configuration setups.
- You can add config values via the command line. The + indicates that the field is new.
    $ python my_app.py +db.driver=mysql +db.user=omry +db.password=secret
    Inside the config.yaml file it'd look like : 
    db:
        driver: mysql
        user: omry
        password: secret

### Hydra_file 
- here the main.py file is differnt 
- the config.yaml file contains default parameters, 
- to pass your own parameters, do the same as above : 
- ``docker run hydra_model 'resnet18' 'https://raw.githubusercontent.com/maxogden/cats/master/cat_photos/00092f6ec7a911e1be6a12313820455d_7.png' ``