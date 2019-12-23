VAR1=$1  # hash
VAR2=$2  #  Directory
mkdir $VAR2
cd $VAR2

swarm down --recursive bzz:/$VAR1

