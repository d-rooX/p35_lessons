import subprocess

res = subprocess.run(('ls', '-l'), capture_output=True)
print(res.stdout.decode('utf-8'))

import requests



