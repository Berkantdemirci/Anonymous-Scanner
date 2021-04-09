# Anonymous-Scanner
Anonymous Scanner is a Privacy oriented port scanning script. It uses tor network with proxychains. A multi-threaded (using concurrent) port scanner that scans top 100 ports.

# Contact Information
  instagram : berkant.py
  
## Installation 

1- Use `git clone https://github.com/Berkantdemirci/Anonymous-Scanner` command to clone the repository.

(attention! scripts must be in the same directory)

2- Required softwares are :

      - Tor
      - proxychains
      - socket
      
  `apt intall tor`
  
  `apt install proxychains`
  
3- You need to configure the proxychains.

Type this to the terminal => `nano /etc/proxychains.conf`

Your configuration settings should look like this.

 ![Screenshot from 2021-04-09 17-49-41](https://user-images.githubusercontent.com/58151582/114198445-febffa00-995b-11eb-90d5-b8428f2ff080.png)

4- After doing all these, you need to configure the torrc.

Type this to the terminal => `nano /etc/tor/torrc`

Your 'torrc' configuration settings should look like this

![Screenshot from 2021-04-09 18-08-51](https://user-images.githubusercontent.com/58151582/114201506-f0bfa880-995e-11eb-9e7d-74557e1b8131.png)

5- Done.

## Usage

Very simple to use. Just run the Anonymous_Scanner.py script.

Example usage 

`sudo service tor start`

`sudo python3 Anonymous_Scanner.py`

![Screenshot from 2021-04-09 18-19-19](https://user-images.githubusercontent.com/58151582/114202813-3f217700-9960-11eb-80fb-70b8fbb6f115.png)

![Screenshot from 2021-04-09 18-21-00](https://user-images.githubusercontent.com/58151582/114202953-611af980-9960-11eb-99c6-d0bfd9ac2ad5.png)

If the script doesn't work properly, try changing the timeout times or contact me. Changing the timeout period will increase the running time of the code. (Speed may vary depending on your internet bandwidth)
