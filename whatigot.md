 virtualenv -p python3 .

source bin/activate

pip install django==2.0.7

Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)
#### make requirements txt
pip freeze > requirements.txt.


django-admin startproject badu

cd badushatest

### make app
at root where manage.py file exist

    python manage.py startapp app name
also add app to setting.py to use



## in case of vscode death
    echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
## run


## imp
while git push in ubuntu u need to use personal acces token u generate rather tha password


## model change
delete all files in migrations folder
delete pycache
delete sqlite


## django shell
 
    on root :
    python manage.py shell

##### import model
    from appname.model import model_class

    ######get all objects of that class
    model_class.objects.all()

    model_class.objects.create(pass values)


## managemet 
    lsof -i :portno
to get process id on portno to kill and free up port 

## python linting fix at vscode in case of extention fail
visit link 
    https://code.visualstudio.com/docs/python/linting
    
    
    
## how to start postgressql
  sudo server start postgrsql
 
  sudo systemctl postgresql start
  
  
  
  
## how to install and set up redis out side pipenv 


  1519  sudo systemctl start postgresql
 1520  sudo systemctl status postgresql
 1521  sudo apt install redis-server
 1522  sudo nano /etc/redis/redis.conf
 1523  sudo  code  /etc/redis/redis.conf
 1524  sudo nano /etc/redis/redis.conf
 1525  sudo systemctl restart redis.service
 1526  sudo systemctl status redis
 1527  redis-server




## pipenv shell setup celary and redis
   pip install celary redis
    celery -A blog22 worker -l info
   
