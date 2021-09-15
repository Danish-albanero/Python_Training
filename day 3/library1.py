from urllib.request import urlopen
with urlopen('https://docs.python.org/3.6/tutorial/stdlib.html') as response:
         for line in response:
             line = line.decode('utf-8') 
             if 'os' in line :  
                 print(line)
