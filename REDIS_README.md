> environment: mac python3.7

###1. get source  
$ wget http://download.redis.io/releases/redis-5.0.0.tar.gz(notice: you must install wget with brew if your mac hasn't)  
$ tar xzf redis-5.0.0.tar.gz  
###2. compile it  
$ cd redis-5.0.0  
$ make  
###3. start server
$ src/redis-server
###4 start client (if you need?)
$ src/redis-cli
then you can interact with redis-server like:  
$ set name ice  
$ get name
  
