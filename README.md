# Innosoft Test

##### Requirements

1. python >= 3.6.3
2. pip >= 19.0.3 
3. opencv-python >= 3.4.0.14, <4.0.0
4. numpy >= 1.16.1   
5. django >= 2.1.7   
6. pytz >= 2018.9

##### Docker
```bash
$ git clone git@github.com:glebasterbajo/InnoTest.git
$ cd InnoTest/
$ docker-compose up --build
```

##### Manual Installation (Ubuntu 18.04)
* install pip
```bash
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
$ sudo pip install virtualenv
```
* clone repository & change dir
```bash
$ git clone git@github.com:glebasterbajo/InnoTest.git
$ cd InnoTest/
```
* create & activate virtualenv
```bash
$ virtualenv venv
$ source venv/bin/activate
```
* install requirements
```bash
$ pip install -r requirements.txt
```
* run main.py to see cup & title detection
```bash
$ python main.py
```
* run web/manage.py to start webapp
```bash
$ python web/manage.py runserver 7777 --noreload
```
**_NOTICE:_**
It takes about 40 seconds to process video. End of processing can be detected by string "Done creating screenshots" in terminal.
* watch the result

Open [http://127.0.0.1:7777/](http://127.0.0.1:7777/)
