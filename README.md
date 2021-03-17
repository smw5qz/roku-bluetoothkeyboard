# roku-bluetoothkeyboard
Python program controlling Roku TV with a bluetooth keyboard.  
*Mappings subject to change across different keyboards  
*Keyboard must be connected to machine running the program prior to program start.  
*Keyboard disconnect will terminate the program (will improve this in later release).  
*Requires: Roku TV, Bluetooth keyboard, Linux machine (preferably raspberry pi or micro pc running Linux)

Install required modules for python3:  
pip3 install keyboard  
pip3 install roku  
pip3 install time  

To run in background on machine:
nohup python3 rokuctl &

