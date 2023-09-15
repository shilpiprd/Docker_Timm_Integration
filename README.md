### Task 
- This Project contains a main.py file which includes code to load a model from timm, and pass an image in that model to get output in json format. 
- Here no training of model is involved, but if needed, a separate ``train.py`` file could be added. 
- The requirements.txt file contains the package requirements which is used by the Dockerfile. 
- The Dockerfile contains the basic instructions in order to build an image. 
- test.sh file contains some basic tests to check whether the build runs, output is in json format or not etc. 

### Commands Required to run the model . 

- ``docker build -t shilpi06/timm . `` 

- ``docker run shilpi06/timm --model 'resnet18' --image 'https://github.com/pytorch/hub/raw/master/images/dog.jpg'``

- The given link above, is a link for the image. 

### Hydra 
- Hydra is a framework developed by Facebook for elegantly configuring complex applications. One of Hydra's primary features is allowes you to dynamically create a hierarchical configuration by composing multiple config files and overriding them from the command line. It's beneficial for applications that have complex configuration setups.

### Hydra_file 
- here the main.py file is differnt 
- the config.yaml file contains default parameters, 
- to pass your own parameters, do the same as above : 
- ``docker run hydra_model --model 'resnet18' --image 'https://github.com/maxogden/cats/blob/master/cat_photos/00092f6ec7a911e1be6a12313820455d_7.png'``