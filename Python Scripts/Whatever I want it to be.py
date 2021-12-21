import subprocess
result = subprocess.run(['whatever'], shell=True)
print(result.stdout)
