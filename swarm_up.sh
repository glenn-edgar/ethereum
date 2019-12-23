VAR1=$1  # file

hash=$(swarm up  $VAR1 2>&1)
echo this is the upload hash "$hash"
