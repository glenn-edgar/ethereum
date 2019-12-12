#echo $1
solcjs --optimize --bin --abi -o solc_output $1
VAR1=$1
VAR2="${VAR1}_HelloWorld.bin"
VAR3="${VAR1}_HelloWorld.abi"
VAR4="${VAR1}.bin"
VAR5="${VAR1}.abi"
#echo "$VAR2"
#echo "$VAR3"
#echo "$VAR4"
#echo "$VAR5"
cd solc_output
mv $VAR2 $VAR4
mv $VAR3 $VAR5