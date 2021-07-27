# import necessary modules
from pwn import *
import json
import glob

# sort the config files present
print('Searching current working directory for \'bandit(x).cfg\' files...')
configList = glob.glob('bandit?.cfg')
configList.sort()
print(f'Found {len(configList)} config files.')
# create password file
passwordFile = open('banditPasswords.txt', 'w')

# start config file loop. Loops over all the cfg files present in the cwd
for i in range(len(configList)):
    with open(configList[i]) as f:
        cfgFile = json.load(f)
        print(f'Reading \'bandit{i}.cfg\'...')

    # set ssh variables
    adr = cfgFile['address']
    prt = cfgFile['port']
    usr = cfgFile['username']

    if i == 0:
        psw = cfgFile['password']
        print(f'Using the password {psw} from \'bandit{i}.cfg\'')
    else:
        with open('banditPasswords.txt', 'r') as file:
            data = file.read()
        passwordFileLines = data.splitlines()
        psw = str(passwordFileLines[i-1])
        psw = psw[-32:]
        print(f'Using most recent password from \'banditPasswords.txt\', which is: \n{psw}')

# SSH using pwn
    print(f'Opening SSH connection to bandit level {i}...')
    shell = ssh(usr, adr, password=psw, port=int(prt))
    sh = shell.run('sh')
# loop over the cmds
    print('Sending commands...')
    cmdsLeft = (len(cfgFile) - 4)
    for cmds in range(cmdsLeft):
        currentCommand = cfgFile[f'cmd{cmds+1}']
        currentCommand = bytes(currentCommand, 'ascii')
        sh.sendline(currentCommand)
        cmdsLeft = cmdsLeft - 1
    nextPass = sh.recvline(timeout=5)
    # convert password bytes to plaintext for sexier storage
    printPass = nextPass.decode('UTF-8')
    printPass = printPass[-33:] # make sure we only print the characters that are a part of the password
    print(f'Got level {i + 1} password!')

# save password to password file
    passwordFile = open('banditPasswords.txt', 'a')
    passwordFile.write(f'The password for bandit labs CTF level {i+1} is: ' + printPass)
    passwordFile.close()
    print(f'Saved level {i + 1} password to banditPasswords.txt in cwd!')

# exit statement
print(f'Program stopped because no other config files were detected. Solved up to level {i + 1}, passwords saved to cwd \'banditPasswords.txt\'. Have a beautiful day.')
passwordFile.close()
