VAR1=$1  # directory

hash=$(swarm --recursive up  $VAR1 2>&1)
echo this is the upload hash "$hash"
