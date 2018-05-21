import subprocess 

print ('$ nslookup www.pythom.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print ('Exit code:', r)