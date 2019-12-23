cd /home/pi/ethereum_apps/

while [ 1 ]
do
   
  ./swarm_node_start.sh    2>  /tmp/swarm.err 
   
  
   mv /tmp/swarm.err /tmp/swarm.errr

done
