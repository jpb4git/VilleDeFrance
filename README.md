# Ville De France [![Build Status](https://travis-ci.com/jpb4git/VilleDeFrance.svg?branch=master)](https://travis-ci.com/jpb4git/VilleDeFrance)

Projet  python 

#### Getting Started
> The overriding design goal for this project
> is to familiarize student to dev with python
> and python environment. 


### Prerequisites

This project is currently extended with the following prerequisites. Instructions on how to install them in your own application are explained below.

| PREREQUISITES |
| ------ |
| python3.7 |
| pip|
| pipenv | 
| jupyter | 
| git | 



### Installing

>installation de python 3.7.4 

go to /usr/src  and wget the desired pythonX.x version  
```
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
```

tar the downloaded file
```
sudo tar xzf Python-3.7.4.tgz
```

go to python folder then we enable the python optimisation
Compile source with [Make]
then we check the python installation   
```
cd Python-3.7.4
sudo ./configure --enable-optimizations
sudo make altinstall
 python3.7 -V
```

>installation de pip
```
 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 python get-pip.py
 sudo python get-pip.py
```


>installation de pipenv


create project with pipenv

don't forget to navigate to the correct folder for your new project
then
```
python3.7 -m pipenv shell
```
>installation jupyter
when you 'r in your env (shell)
you can run this command to install jupyter 
```
pipenv install jupiter
```

now we can launch Jupyter  notebook application with 
```
jupiter notebook
```
## Dependencies

[packages]
>jupyter 
>pandas 
>matplotlib 
>csv 

## Running the tests

   Explain how to run the automated tests for this system

### Break down into end to end tests

   Explain what these tests test and why

   ```
    Give an example
   ```

### And coding style tests

    Explain what these tests test and why

    ```
    Give an example
    ```

## Deployment


## Built With

* [Jupiter](https://jupyter.org/documentation) - The web framework used

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **jpb4GIt** - *Initial work* - (https://github.com/jpb4git/)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration

