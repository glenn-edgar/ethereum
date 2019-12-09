cd /home/pi/ethereum_apps/redis
while [ 1 ]
do
   
   redis-server redis.conf    2>  /tmp/redis_server.err 
   
  
   mv /tmp/redis_server.err /tmp/redis_server.errr

done
