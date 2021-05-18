# L2L's Django Technical Interview

This repository contains a project used by the L2L Engineering team for technical interviews. The goal of this exercise 
is to evaluate how you would do in adding a custom Django filter. If you are experienced in Django this may seem like a
very simple exercise. That's good. If you are new to Django but experienced in programming in general and specifically in web 
technologies this may require some digging through documentation which is also good. If you are new this may take up to 
an hour. If you find that this exercise takes longer than 60 minutes you may want to reach out to your L2L contact to 
see if there is a misunderstanding in the directions or we may have a bug in our documentation below. The intent is not
to take a ton of your time so please reach out if you find something difficult or incompatible with your environment.

In order to complete this exercise the first thing you will need to do is fork this repo to your own personal github 
repo. Once you have done that you can continue the exercise. This exercise can be completed on any modern OS using a 
terminal (Windows (use wsl), OSX, Linux, etc). After forking this repo, clone your repo down to your own computer. If 
you are new to programming this is a great resource: 
[github docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository "github docs")

On your computer you will want to create a python virtual environment in order to contain the libraries necessary to 
run the example web application. In your cloned repo directory run the following commands:
- `$ which python3`
- `$ <output of previous command> -m venv l2lpyenv`
- `$ . ./l2lpyenv/bin/activate`
- `$ pip install Django==3.2.3`
- `$ python manage.py runserver 0.0.0.0:8080`

You should now see output indicating that the Django site is running. If you run into a situation where you are told 
that the version of sqlite is not compatible with the Django version you are running you can run the following 
commands. If everything is working, skip over these steps.
- `$ wget https://www.sqlite.org/2018/sqlite-autoconf-3240000.tar.gz`
- `$ tar zxvf sqlite-autoconf-3240000.tar.gz`
- `$ cd sqlite-autoconf-3240000/`
- `$ ./configure --prefix=/usr/local`
- `$ make`
- `$ sudo make install`

If you needed to run the above steps for sqlite then you will want to run the following command before starting django 
with the runserver command:
- `$ export LD_LIBRARY_PATH=/usr/local/lib`
- `$ python manage.py runserver 0.0.0.0:8080`

At this point you will only need to run the runserver command in order to start the web server. If you go to a browser 
you can now open the main page served by the web server by entering something like `http://localhost:8080/` into the 
url address bar. Congrats you can follow directions :-)

You are now set to work on adding a custom Django filter to the application. If you look inside 
l2l/templates/l2l/index.html on lines 60 and 61 there are two comments. You need to figure out how to create custom 
filter and write the code that implements the l2l_dt filter. You will need to uncomment line 2 of index.html as well in
order to register the filter with the template. Feel free to name your filter whatever you'd like. The l2l_extras 
template tag and the l2l_dt filter names are what we used in creating the exercise. Your filter needs to handle receiving a date object and a 
string. The string format will be in the following format: `"%Y-%m-%dT%H:%M:%S"`. Your filter should print the results 
in the following format: `"%Y-%m-%d %H:%M:%S"`. You will know you have succeeded when you can hit the main web page 
after removing the comments on lines 60 and 61 and the browser shows the results accurately.

L2L is a completely remote work environment. We utilize a lot of remote technology to communicate and stay up-to-date 
with each other. Instead of creating a pull request, the correct thing to do now is push your local changes up to your 
forked repo, then create a short [loom video](https://www.loom.com/ "loom video") showing the end result, talking 
through any interesting decisions or directions you took, and finally send an email with a link to your commit and a 
link to your loom video to the L2L employee you are coordinating this exercise with.
