cd /home/pi/ethereum_apps/
while [ 1 ]
do
   
   ./dev_start.sh    2>  /tmp/ethereum.err 
   
  
   mv /tmp/ethereum.err /tmp/ethereum.errr

done
