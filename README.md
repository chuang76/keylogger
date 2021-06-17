# keylogger

Disclaimer: This project is for educational purposes only. 

This project consists of three stages, reconnaissance, phishing, and attack, respectively. During the reconnaissance stage, the attacker collects target email addresses and uses ARP scan to obtain target IPs. Next, during the phishing stage, the attacker sends phishing emails that contain the link of the phishing website (fake Microsoft patching website in our case) to the victims. The downloader in the phishing website will redirect to the link of malware. If the victims follow the instructions, that is, download and run the executable (malware actually), the executable will start logging the keystrokes and create a backdoor shell. So the attacker can use the backdoor to retrieve a log file that contains some sensitive data. 



## Environment

- Kali Linux VM
- Windows Server 2016 VM
- Visual Studio C++ build tools 



## Usage of keylogger 

To achieve a keylogging attack, compile .cpp files in the malware folder, then executable the run.bat file. 

```
$ cl /EHsc <file name>
```

For the attacker, run the following command. 

```
$ nc <victom IP> 1234
```



## Result

