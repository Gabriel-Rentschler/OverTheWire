import subprocess
import os

#proc = subprocess.Popen(["nc vortex.labs.overthewire.org 5842"], stdout=subprocess.PIPE, shell=True)
#(out, err) = proc.communicate()

#out = subprocess.check_output(['nc', 'vortex.labs.overthewire.org', '5842'])

#out = subprocess.run(['nc', 'vortex.labs.overthewire.org', '5842'], stdout=subprocess.PIPE)

os.system('echo > /tmp/level0dump')
dumpsize = os.path.getsize('/tmp/level0dump')

os.system('nc vortex.labs.overthewire.org 5842 > /tmp/level0dump &')
while (dumpsize <= 1):
    dumpsize = os.path.getsize('/tmp/level0dump')

#os.system('kill -s 3 $!')
print(dumpsize)

output = open('/tmp/level0dump', 'rb')

print(output.read())
