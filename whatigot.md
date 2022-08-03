 virtualenv -p python3 .

source bin/activate

pip install django==2.0.7

django-admin startproject badu

cd badushatest




##in case of vscode death
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
##run


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
to get process id on portno

