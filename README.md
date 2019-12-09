# Ville De France

Projet  python 

## Getting Started



### Prerequisites

python3.7
pip
pipenv
jupyter


### Installing

 

installation de python 3.7.4 

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

installation de pip
```
 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 python get-pip.py
 sudo python get-pip.py
```


installation de pipenv


create project with pipenv



don't forget to navigate to the correct folder for your new project
then
```
python3.7 -m pipenv shell
```
installation jupyter
when you 'r in your env (shell)
you can run this command to install jupyter 
```
pipenv install jupiter
```

now we can launch Jupyter  notebook application with 
```
jupiter notebook
```

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

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

